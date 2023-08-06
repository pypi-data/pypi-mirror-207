import ast
import inspect
from copy import deepcopy
from functools import partial
from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field
from fluidsdk.conversational_modules import OpenAIGPTConfig

from fluidsdk.intents import (
    AskDefiniteIntent,
    AskOpenIntent,
    GPTGenerateIntent,
    HTTPBody,
    HTTPRequestConfig,
    HTTPRequestIntent,
    SayIntent,
)
from fluidsdk.message import Message
from fluidsdk.pyrite import utils
from fluidsdk.pyrite.consts import ASK_AND_ACK_PRE_PROMPT
from fluidsdk.pyrite.message import parse_message, parse_messages
from fluidsdk.status_webhook import StatusIntentData
from fluidsdk.templates import GPTGenerateTemplate


def say(*messages: Message) -> None:
    """
    Say a list of messages.

    :param messages: One or more messages to say.
    """

    def builder(context, node):
        # Raises an error if the keyword arguments are present.
        if node.keywords:
            utils.raise_type_error(
                context.source_lines,
                context.filename,
                node.keywords,
                "`say` does not take any keyword arguments.",
            )

        utils.insert_then_increment(
            context,
            context.idx,
            SayIntent(text=list(parse_messages(context, node.args))),
        )

    return builder


def ask(*messages: Message) -> str:
    """
    Send a list of messages, and return the user's response.

    :param messages: One or more messages to say.

    :return: The user's response
    """

    def builder(context, node, target_field):
        if node.keywords:
            utils.raise_type_error(
                context.source_lines,
                context.filename,
                node.keywords,
                "`ask` does not take any keyword arguments.",
            )

        utils.insert_then_increment(
            context,
            context.idx,
            AskDefiniteIntent(
                question=list(parse_messages(context, node.args)),
                answer_field=target_field,
            ),
        )

    return builder


class Context:
    def __init__(self):
        """
        Flow Step Context Manager.
        """
        pass

    def __call__(self, context_manager, body, context, context_name):
        self.context_manager = context_manager
        self.body = body
        self.context = context
        self.context.step_contexts[context_name] = self
        self.steps = []
        self.active = False
        return self

    def with_body(self, body, context):
        self.body = body
        self.context = context
        return self

    def __enter__(self) -> "Context":
        self.active = True
        body_context = deepcopy(self.context)
        body_context.builder = self.context.builder
        body_context.step_contexts = self.context.step_contexts
        body_context.idx = 1
        self.body_context = body_context
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.active = False

        self.context.idx += 1

        self.context
        self.context.global_names.update(self.body_context.global_names)
        self.context.local_names.update(self.body_context.local_names)
        self.context.step_contexts.update(self.body_context.step_contexts)

        self.context.flow_steps.update(self.body_context.flow_steps)

    def add_step(self, step, intent):
        if self.active:
            self.steps.append(step)

    def acknowledge(self):
        def builder(context, node):
            target_field = "acknowledgement-" + context.prefix + "-" + str(context.idx)
            utils.insert_then_increment(
                context,
                context.idx,
                GPTGenerateIntent(
                    template=GPTGenerateTemplate(
                        template_id="pyrite_acknowledge",
                        re="([\s\S]*)Person B:([\s\S]*)",
                        results=["reasoning", "acknowledgement"],
                        default_on_failure={
                            "reasoning": "I didn't understand :/",
                            "acknowledgement": utils.one_of(
                                [
                                    "Oo, Understood!",
                                    "That’s quite something really.",
                                    "Got it",
                                ]
                            ),
                        },
                        pre_prompt=ASK_AND_ACK_PRE_PROMPT,
                        user_prefix="Person A:",
                        bot_prefix="Person B:",
                        post_prompt="Explanation:",
                        gpt_config=OpenAIGPTConfig(
                            engine="text-davinci-003",
                            temperature=0.2,
                            max_tokens=120,
                            stop=["###", "Tip", "Acknowledgment", "\n\n"],
                            # logit_bias={"50256": -25},
                        ),
                    ),
                    collect=self.steps,
                    answer_field="data_stack.[{py>len(data_stack)-1}]." + target_field,
                ),
            )
            utils.insert_then_increment(
                context,
                context.idx,
                SayIntent(
                    text=[
                        '[{py>data_stack[-1]["'
                        + target_field
                        + '"]["acknowledgement"]}]'
                    ]
                ),
            )

        return builder

    exports = {
        "statement_library": ["acknowledge"],
    }


def GPTGenerate(
    template: str, context: Optional[Context] = None, args: Dict[str, str] = None
) -> Dict:
    """
    Use a Large Language Model to generate text.

    :param template: The name of the template to use. Must be a valid Python identifier in the context's templates dictionary.
    :param context: The context in which the template is to be generated.
    :param args: A dictionary of arguments to pass to the template.

    :return: The results of the generation as a dictionary
    """

    def builder(context, node, target_field):
        raise_syntax_error = partial(
            utils.raise_syntax_error, context.source_lines, context.filename
        )

        raise_type_error = partial(
            utils.raise_type_error, context.source_lines, context.filename
        )

        signature = inspect.signature(GPTGenerate)
        args = utils.test_signature(
            signature,
            node.args,
            node.keywords,
            partial(raise_type_error, node),
        ).arguments
        # Check that template argument is a constant

        utils.assert_constant_type(
            args["template"],
            str,
            raise_type_error,
            "template must be of type str.",
        )
        template_id = args["template"].value
        # Check if the template_id is valid.
        if template_id not in context.builder.templates:
            utils.raise_template_error(
                context.source_lines,
                context.filename,
                args["template"],
                f"Invalid template {template_id}. Did you include this template?",
            )

        # Check that the context argument is a variable name.
        if args["context"] is None:
            steps = []
        else:
            utils.assert_node_type(
                args["context"],
                ast.Name,
                raise_syntax_error,
                "context must be a variable name.",
            )
            context_name = args["context"].id
            # Raise syntax error if the context is undefined.
            if context_name not in context.step_contexts:
                raise_syntax_error(
                    args["context"],
                    f"Undefined context {context_name}.",
                )
            steps = context.step_contexts[context_name].steps

        ask_open_args = {}
        if args["args"] is not None:
            utils.assert_node_type(
                args["args"],
                ast.Dict,
                raise_syntax_error,
                "args must be a dictionary.",
            )
            for k, v in zip(args["args"].keys, args["args"].values):
                utils.assert_constant_type(
                    k,
                    str,
                    raise_syntax_error,
                    "args keys must be strings.",
                )
                ask_open_args[k.value] = (
                    "[{py>" + utils.build_expression(v, context.prefix, context) + "}]"
                )
        utils.insert_then_increment(
            context,
            context.idx,
            GPTGenerateIntent(
                template=template_id,
                collect=steps,
                answer_field=target_field,
                args=ask_open_args,
            ),
        )

    return builder


def AskOpen(
    question: str, turns: int, template: str, dynamic_stop_regex: Optional[str] = None
) -> List:
    """
    Use a Large Language Model hold a short conversation

    :param question: First message.
    :param turns: Number of turns this conversation should last.
    :param template: The name of the AskOpen template to use.
    :param dynamic_stop_regex: Regex to stop the conversaion once bot generates this trigger.

    :return: The turns of the conversation as a list. Includes the question, user's response, and the bot's inference,
    """

    def builder(context, node, target_field):
        raise_syntax_error = partial(
            utils.raise_syntax_error, context.source_lines, context.filename
        )

        raise_type_error = partial(
            utils.raise_type_error, context.source_lines, context.filename
        )

        signature = inspect.signature(AskOpen)
        args = utils.test_signature(
            signature,
            node.args,
            node.keywords,
            partial(raise_type_error, node),
        ).arguments
        # Check that template_id is of type str.
        utils.assert_constant_type(
            args["template"],
            str,
            raise_type_error,
            "template must be of type str.",
        )

        template_id = args["template"].value

        utils.assert_constant_type(
            args["turns"],
            int,
            raise_type_error,
            "turns must be of type int.",
        )
        turns = args["turns"].value
        if args["dynamic_stop_regex"] is not None:
            utils.assert_constant_type(
                args["dynamic_stop_regex"], Optional[str], raise_type_error
            )
            dynamic_stop_regex = args["dynamic_stop_regex"].value
        else:
            dynamic_stop_regex = None

        # Check if the template_id is valid.
        if template_id not in context.builder.templates:
            utils.raise_template_error(
                context.source_lines,
                context.filename,
                args["template"],
                f"Invalid template {template_id}. Did you include this template?",
            )

        utils.insert_then_increment(
            context,
            context.idx,
            AskOpenIntent(
                template=template_id,
                followups=turns,
                question=parse_message(context, args["question"]),
                answer_field=target_field,
                dynamic_stop_regex=dynamic_stop_regex,
            ),
        )

    return builder


_exports = {
    "context_library": [Context],
    "statement_library": [say],
    "assignment_library": [ask, GPTGenerate, AskOpen],
}


def HTTPRequest(
    url: str,
    body: HTTPBody,
    config: HTTPRequestConfig,
    method: Literal["GET", "POST"] = "GET",
    headers: Dict[str, str] = {},
    params: Dict[str, str] = {},
    response_type: Literal["text", "json"] = "json",
):
    """
    Make an HTTP Request

    :param url: URL to make the request to.
    :param method: HTTP method to send the request with.
    :param headers: Headers to include in the request.
    :param param: URL Encided Parameters to be included in the request.
    :param body: Body to be included in the request
    :param response_type: Type to interpret the response body as.
    :param config: Config options for HTTP Request
    """

    def builder(context, node, target_field):
        raise_type_error = partial(
            utils.raise_type_error, context.source_lines, context.filename
        )

        signature = inspect.signature(AskOpen)
        args = utils.test_signature(
            signature,
            node.args,
            node.keywords,
            partial(raise_type_error, node),
        ).arguments

        url = utils.build_expression(args["url"], context.prefix, context)

        utils.insert_then_increment(
            context,
            context.idx,
            HTTPRequestIntent(
                url=url,
                answer_field=target_field,
            ),
        )

    return builder
