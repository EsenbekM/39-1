import logging
import time

from django.http import HttpResponseForbidden
from django.shortcuts import redirect


logger = logging.getLogger(__name__)


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("before request")

        response = self.get_response(request)
        
        print("after request")

        return response
    

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Request: {request.method} {request.path}")

        response = self.get_response(request)

        logger.info(f"Response: {response.status_code}")

        return response
    

class BlacklistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

        print(ip)

        if ip in ['127.0.0.1']:
            return HttpResponseForbidden()
        
        response = self.get_response(request)

        return response
    

class PerformanceMonitoringMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        print(f"Request to {request.path} took {duration} seconds")
        return response
    


class URLRewritingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if '/old-url/' in request.path:
            # Перенаправление с старого URL на новый URL
            return redirect('/new-url/')
        return self.get_response(request)