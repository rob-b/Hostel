from functools import update_wrapper, wraps

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def rendered(func):
    """Decorator to simplify returning RequestContext"""
    @wraps(func)
    def render_function(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if isinstance(response, HttpResponse) or isinstance(response,
                                                            HttpResponseRedirect):
            return response
        template_name, items = response
        return render_to_response(template_name, items,
                                  context_instance=RequestContext(request))
    return render_function


def access_allowed(test_func, redirect_url=None):
    """
    decorate views by making sure that a user passes a test function that will
    then allow them access to that view. test_func must be a callable that
    takes a user instance as its only argument and returns a boolean.

    This differs from django.contrib.auth.decorators.user_passes_test in that
    this does not push users who fail the test to a login page
    """
    def decorate(view_func):
        def wrapper(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return update_wrapper(wrapper, view_func)
    return decorate

def redirect_to_profile(f):
    def wrapper(request, **kwargs):
        response = f(request, **kwargs)
        if isinstance(response, HttpResponseRedirect) and \
           request.user.is_authenticated():
            if 'next' in request.GET:
                destination = request.GET['next']
            else:
                profile = request.user.get_profile()
                destination = profile.get_absolute_url()
            return HttpResponseRedirect(destination)
        return response
    return update_wrapper(wrapper, f)


def set_language(f):
    from django.utils import translation
    def wrapper(*args, **kwargs):
        language = translation.get_language()
        translation.activate(language)
        return f(*args, **kwargs)
    return update_wrapper(wrapper, f)

