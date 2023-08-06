import collections
import os

from django import template
from django.conf import settings
from django.apps import apps
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.template.base import Lexer, Parser
from django.template.loader_tags import construct_relative_path
from django.templatetags.static import static

from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse, quote

from ..apps import get_app_label
from ..tags import register_simple_block_tag, parse_tag
from ..more_tags import ExtendWithCustomBlocksNode

__all__ = ['concat_tag', 'no_script_redirect', 'discover_installed_support_tags', 'tagged_static']


APP_LABEL = get_app_label()

register = template.Library()


@register.simple_tag(name="concat")
def concat_tag(*args):

    result = ''

    for arg in args:
        if not arg and arg != 0:
            continue

        result += str(arg)

    return result


@register.tag(name="no_script_redirect")
def no_script_redirect(parser, token):

    is_valid = True

    if is_valid:
        return NoScriptRedirectNode()
    else:
        raise template.TemplateSyntaxError(
            "'noscript_redirect' tag syntax error."
        )


class NoScriptRedirectNode(template.Node):
    def __init__(self):
        pass

    def render(self, context):

        try:
            request = context['request']
        except template.VariableDoesNotExist:
            return ''

        noscript = request.GET.get('noscript', None)

        if noscript is None:
            url = request.build_absolute_uri()
            parsed_url = urlparse(url)
            parameters = parse_qsl(parsed_url.query)
            parameters.append(('noscript','true')) # noqa
            parsed_url = parsed_url._asdict()
            parsed_url['query'] = urlencode(parameters)
            url = urlunparse(parsed_url.values())
            result = format_html('<noscript><meta http-equiv="refresh" content="0;url={}"></noscript>', url)
        else:
            result = ''

        return result


app_labels_by_module = {}


def map_modules_to_app_labels():

    global app_labels_by_module
    app_labels_by_module = {}

    for app_label, app_config in apps.app_configs.items():
        app_labels_by_module[app_config.name] = app_label


installed_support_tags = collections.OrderedDict()


def discover_installed_support_tags():

    result = {}

    for template_engine in template.engines.all():

        engine = template_engine.engine

        for identifier, library in engine.template_libraries.items():

            prefix, sep, suffix = identifier.rpartition('_tags')

            if not sep or suffix:
                continue

            identifier = prefix

            if identifier not in apps.app_configs:
                continue

            tag_name = identifier + "_support"

            if tag_name not in library.tags:
                continue

            result[identifier] = tag_name, library.tags[tag_name]

    global installed_support_tags

    installed_support_tags = collections.OrderedDict()

    installed_apps = getattr(settings, 'INSTALLED_APPS', [])

    for app_module in installed_apps:

        app_label = app_labels_by_module.get(app_module, None)

        if app_label is None:
            continue

        tag_entry = result.get(app_label, None)

        if tag_entry is None:
            continue

        installed_support_tags[app_label] = tag_entry

    return None


@register.simple_tag(takes_context=True)
def include_app_support(context, *, container_element, include=None, exclude=None):

    if not include:
        include = ''

    if not exclude:
        exclude = ''

    include = include.split()
    exclude = exclude.split()

    labels = include or exclude
    include_labels = bool(include)

    result = mark_safe('')

    for app_label, tag_entry in installed_support_tags.items():

        if include_labels != (app_label in labels):
            continue

        tag_name, tag_function = tag_entry

        pseudo_template = "{{% {} container_element='{}' %}}".format(tag_name, container_element)
        lexer = Lexer(pseudo_template)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        parser.tags[tag_name] = tag_function

        nodelist = parser.parse()
        result += nodelist.render(context)

    return result


@register.simple_tag(name="wrap_as_list")
def wrap_as_list_tag(*args):
    return list(args)


@register.simple_tag(name="list_separator_prefix", takes_context=True)
def list_separator_prefix_tag(context, *, loop=None, default_separator=', ', last_separator=' and '):

    if loop is None:
        loop = context['forloop']

    if not loop['counter0']:
        return ''

    if loop['last']:
        return last_separator

    return default_separator


@register.simple_tag(name="tagged_static")
def tagged_static(path, version=None):
    return static(path)


@register.simple_tag(name="join_pair")
def join_pair_tag(*, left, right, separator=' ', left_suffix='', right_prefix='', placeholder=''):

    if left and right:
        return left + separator + right

    if left:
        return left + left_suffix

    if right:
        return right_prefix + right

    return placeholder


@register.filter
def split_ext(value):
    return os.path.splitext(value)[1]


@register.filter
def basename(value):
    return os.path.basename(value)


@register.tag(name='extend_with_custom_blocks')
def parse_extend_with_custom_blocks_tag(parser, token):

    bits = token.split_contents()
    tag_name = bits[0]

    if len(bits) != 4:
        raise template.TemplateSyntaxError(
            "'%s' expects a template name argument followed by a block list argument" % tag_name
        )

    template_name = bits[1]
    custom_blocks = bits[2]
    name_suffix = bits[3]

    nodelist = parser.parse()

    if nodelist.get_nodes_by_type(ExtendWithCustomBlocksNode):
        raise template.TemplateSyntaxError(
            "'%s' cannot appear more than once in the same template" % tag_name
        )

    template_name = construct_relative_path(parser.origin.template_name, template_name)
    template_name = parser.compile_filter(template_name)
    custom_blocks = parser.compile_filter(custom_blocks)
    name_suffix = parser.compile_filter(name_suffix)

    node = ExtendWithCustomBlocksNode(nodelist, template_name, custom_blocks=custom_blocks, name_suffix=name_suffix)
    return node
