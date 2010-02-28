from django.http import HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext, loader


def forbidden(request, template_name='403.html'):
    response = render_to_response(template_name,
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response


def server_error(request, template_name='500.html'):
    t = loader.get_template(template_name)
    c = RequestContext(request)
    return HttpResponseServerError(t.render(c))
