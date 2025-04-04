# store/middleware.py

import time
from django.utils.deprecation import MiddlewareMixin
from .models import Category

class CategoryViewTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

        if request.path.startswith('/category/'):
            slug = request.path.strip('/').split('/')[-1]
            try:
                category = Category.objects.get(slug=slug)
                category.view_count += 1
                category.save()
            except Category.DoesNotExist:
                pass

    def process_response(self, request, response):
        if hasattr(request, 'start_time'):
            duration = time.time() - request.start_time
            request.duration = duration
            if hasattr(response, 'context_data'):
                response.context_data['request_duration'] = f"{duration:.2f}"
        return response
