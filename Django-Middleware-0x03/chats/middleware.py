# chats/middleware.py

from datetime import datetime, time
import logging
import os
from django.http import HttpResponseForbidden

# Set up logger
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, 'requests.log')

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(message)s'
)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_entry = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logging.info(log_entry)

        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define allowed access window: 6:00 PM to 9:00 PM
        now = datetime.now().time()
        allowed_start = time(18, 0)  # 6:00 PM
        allowed_end = time(21, 0)    # 9:00 PM

        # Restrict only /chat/ or /api/chat/ paths (optional for scope control)
        if request.path.startswith('/chat') or request.path.startswith('/api/chat'):
            if not (allowed_start <= now <= allowed_end):
                return HttpResponseForbidden("Chat is only accessible between 6:00 PM and 9:00 PM.")

        return self.get_response(request)