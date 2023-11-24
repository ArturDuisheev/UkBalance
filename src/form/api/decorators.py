from functools import wraps
from rest_framework import status
from rest_framework.response import Response

import time


def range_limit(limit, period_of_block):
    def decorator(view_func):
        request_history = []

        @wraps(view_func)
        def wrapper(*args, **kwargs):
            current_time = time.time()

            request_history[:] = [timestamp for timestamp in request_history if
                                  timestamp > current_time - period_of_block]

            if len(request_history) >= limit:
                return Response(
                    {'error': 'Too many requests, please try again'}, status=status.HTTP_429_TOO_MANY_REQUESTS
                )

            request_history.append(current_time)
            return view_func(*args, **kwargs)

        return wrapper

    return decorator
