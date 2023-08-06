from inspect import getfullargspec

from django.template.library import parse_bits, TagHelperNode
from django.utils.html import conditional_escape
from django.template.exceptions import TemplateSyntaxError

__all__ = ['parse_tag', 'register_simple_block_tag']


def parse_tag(func, name, takes_context, takes_nodelist, allows_as, parser, token):
    bits = token.split_contents()[1:]

    target_var = None

    if allows_as and len(bits) >= 2 and bits[-2] == "as":
        target_var = bits[-1]
        bits = bits[:-2]

    # noinspection SpellCheckingInspection
    (
        params,
        varargs,
        varkw,
        defaults,
        kwonly,
        kwonly_defaults,
        _,
    ) = getfullargspec(func)

    if takes_context:
        if params and params[0] == "context":
            params = params[1:]
        else:
            raise TemplateSyntaxError(
                "'%s' takes a context so it must "
                "have a first argument of 'context'" % name
            )

    if takes_nodelist:
        if params and params[0] == "nodelist":
            params = params[1:]
        else:

            if takes_context:
                msg = "takes a context and a nodelist so it must have a second "
            else:
                msg = "takes a nodelist so it must have a first "

            raise TemplateSyntaxError(
                ("'%s' " + msg + "argument of 'nodelist'") % name
            )

    args, kwargs = parse_bits(
        parser,
        bits,
        params,
        varargs,
        varkw,
        defaults,
        kwonly,
        kwonly_defaults,
        False,
        name
    )

    return args, kwargs, target_var


class SimpleBlockNode(TagHelperNode):

    def __init__(self, func, args, kwargs, target_var, nodelist, autoescape):
        super().__init__(func, True, args, kwargs)
        self.target_var = target_var
        self.nodelist = nodelist
        self.autoescape = autoescape

    def render(self, context):

        resolved_args, resolved_kwargs = self.get_resolved_arguments(context)

        # Insert nodelist as second argument after context
        resolved_args.insert(1, self.nodelist)

        output = self.func(*resolved_args, **resolved_kwargs)

        if self.target_var is not None:
            context[self.target_var] = output
            return ""

        if self.autoescape and context.autoescape:
            output = conditional_escape(output)

        return output


# noinspection SpellCheckingInspection
def register_simple_block_tag(register, name=None, autoescape=True):
    def decorator(func):
        tag_name = name or func.__name__

        def tag_adapter(parser, token):
            nodelist = parser.parse(('end' + tag_name,))
            args, kwargs, target_var = parse_tag(func, tag_name, True, True, True, parser, token)
            node = SimpleBlockNode(func, args, kwargs, target_var, nodelist, autoescape)
            parser.delete_first_token()
            return node

        return register.tag(tag_name, tag_adapter)

    return decorator
