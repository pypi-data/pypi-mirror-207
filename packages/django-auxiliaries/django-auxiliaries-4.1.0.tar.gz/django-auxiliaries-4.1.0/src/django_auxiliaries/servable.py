
from django.template.response import TemplateResponse

from .requests import is_ajax


__all__ = ['Servable']


class Servable:

    template = None
    ajax_template = None

    def get_context(self, request):

        context = {
            'request': request,
            'self': self
        }

        return context

    def get_template(self, request):

        if is_ajax(request):
            return self.ajax_template or self.template
        else:
            return self.template

    def serve(self, request):

        response = TemplateResponse(
            request,
            self.get_template(request),
            self.get_context(request),
        )

        return response
