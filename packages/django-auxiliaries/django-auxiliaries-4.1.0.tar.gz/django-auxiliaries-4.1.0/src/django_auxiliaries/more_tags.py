import re


from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.template.base import Lexer, Parser
from django.template.loader_tags import BlockNode, ExtendsNode
from django.template.library import Node, Template


class ExtendWithCustomBlocksNode(ExtendsNode):

    must_be_first = False

    def __init__(self, nodelist, parent_name, template_dirs=None, custom_blocks=None, name_suffix=None):
        super().__init__(nodelist, parent_name, template_dirs)

        begin_regexp = r'{#\s+begin_custom_blocks\s+#}'
        end_regexp = r'{#\s+end_custom_blocks\s+#}'

        if isinstance(begin_regexp, str):
            begin_regexp = re.compile(begin_regexp)

        if isinstance(end_regexp, str):
            end_regexp = re.compile(end_regexp)

        self.begin_regexp = begin_regexp
        self.end_regexp = end_regexp
        self.custom_blocks = custom_blocks
        self.name_suffix = name_suffix

    def get_parent(self, context):

        template = super().get_parent(context)

        block_definitions = ''

        custom_blocks = self.custom_blocks.resolve(context)
        name_suffix = self.name_suffix.resolve(context)

        if isinstance(custom_blocks, dict):
            for name, definition in custom_blocks.items():

                if name_suffix:
                    name = name + name_suffix

                block_definitions += "{{% block {name} %}}\n{definition}\n{{% endblock %}}\n".format(
                    name=name, definition=definition)

        begin_match = self.begin_regexp.search(template.source)
        end_match = self.end_regexp.search(template.source)

        if not begin_match or not end_match or begin_match.start() >= end_match.start() or not block_definitions:
            return template

        modified_source = template.source[:begin_match.start()] + block_definitions + template.source[end_match.end():]

        customized_template = Template(modified_source,
                                       origin=template.origin,
                                       name=template.name,
                                       engine=template.engine)

        return customized_template

    def render(self, context):
        return super().render(context)
