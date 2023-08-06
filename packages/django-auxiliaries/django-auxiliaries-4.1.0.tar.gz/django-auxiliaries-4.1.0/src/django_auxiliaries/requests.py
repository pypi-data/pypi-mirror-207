
__all__ = ['is_ajax']


def is_ajax(request):

    return request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or \
            request.headers.get('x-requested-with') == 'XMLHttpRequest'

