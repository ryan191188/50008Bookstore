from functools import wraps

from django.db import DatabaseError
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied


def json_response(func):
    """Decorator to respond with JSON from a request."""

    @wraps(func)
    def decorator(request, *args, **kwargs):
        status = 500

        try:
            data = func(request, *args, **kwargs)

            if isinstance(data, type(i for i in ())):
                data = tuple(data)

            status = 200
        except PermissionDenied as e:
            data = {
                'error': 'PermissionDenied',
                'detail': str(e),
            }
            status = 403
        except DatabaseError as e:
            data = {
                'code': e.args[0],
                'error': type(e).__name__,
                'detail': ' '.join(e.args[1:]),
            }

        if isinstance(data, JsonResponse):
            return data

        req = ('data', 'error')
        if not isinstance(data, dict) or all(k not in data for k in req):
            data = {'data': data}

        return JsonResponse(data, status=status)

    return decorator
