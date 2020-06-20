from django.http import HttpResponseBadRequest


def ajax_required(func):
    def wrap(request, *args, **kwargs):
        if request.is_ajax():
            return func(request, *args, **kwargs)
        else:
            return HttpResponseBadRequest()
    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap
