from django.conf import settings
from django.shortcuts import redirect

class CheckOrySessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if 'ory_kratos_session' not in request.COOKIES:
            composed_url = settings.ORY_UI_URL + "/login?return_to=http://%s%s" % (request.META['HTTP_HOST'], request.META['PATH_INFO'])
            return redirect(composed_url)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response