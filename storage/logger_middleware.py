# @Time     :2021/11/5 10:14
# @Author   :dengyuting
# @File     :logger_middleware.py
import time
import logging

#取当前脚本名称
logger = logging.getLogger(__name__)

def logger_middleware(get_response):

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        start_time = time.time()

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        duration = time.time() - start_time
        response['X-Page-Duration-ms'] = int(duration * 1000)
        ##根据http请求携带的参数以及报文信息创建一个WSGIRequest对象
        logger.info("%s %s %s %s", duration, request.path, request.method, request.GET.dict())
        return response

    return middleware