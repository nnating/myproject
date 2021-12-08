# @Time     :2021/11/5 14:16
# @Author   :dengyuting
# @File     :mymiddleware.py
import logging
import time
import traceback

from django.http import HttpResponse
from sentry_sdk import capture_message, capture_exception

logger = logging.getLogger(__name__)

class loggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        start_time = time.time()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        duration = time.time() - start_time
        response['X-Page-Duration-ms'] = int(duration * 1000)
        if duration > 0:
            capture_message('slow url: %s  time: %s' % (request.path, duration))

        return response

    def process_exception(self, request, exception):
        print(exception)
        if exception:
            message = "url:      {url} ** msg:     {error}     \----------     {tb}      ---------".format(
                url=request.build_absolute_uri(),
                error=repr(exception),
                tb=traceback.format_exc()
            )

            logger.warning(message)

            # send dingtalk message
            # dingtalk.send(message)

            # capture exception to sentry:
            capture_exception(exception)

        return HttpResponse("Error processing the request, please contact the system administrator.", status=500)