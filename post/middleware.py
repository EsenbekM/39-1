import logging
import time

from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import redirect


class SimleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.path)

        response = self.get_response(request)
        
        print(response.status_code)

        return response
    
logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"Path: {request.path}, Method: {request.method}")
        
        response = self.get_response(request)
        
        logger.info(f"Status code: {response.status_code}")

        return response
    

class BlacklistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')

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

class URLRewriteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/posts/':
            return redirect('/posts2/')

        response = self.get_response(request)
        return response
