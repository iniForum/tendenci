from threading import local

from django.utils.deprecation import MiddlewareMixin

_thread_locals = local()


def get_current_request():
    return getattr(_thread_locals, 'request', None)


class RequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        _thread_locals.request = request
