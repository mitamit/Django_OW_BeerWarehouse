#ejemplo de middleware, deniega el acceso a ciertos usuarios. Criterios admin o no
from django.core.exceptions import PermissionDenied

def access_denied_not_admins(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.user.is_superuser:
            raise PermissionDenied
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware