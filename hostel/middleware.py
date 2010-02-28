from django.http import HttpResponseForbidden


class AuthorizationMiddleware(object):

    def process_response(self, request, response):
        if isinstance(response, HttpResponseForbidden):
            from hostel.views import forbidden
            return forbidden(request)
        else:
            return response


class SetTestCookieMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            request.session.set_test_cookie()


