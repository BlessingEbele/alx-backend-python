# chats/middleware.py

from datetime import datetime, time
import time as time_module
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

        current_time = time_module.time() #for UNIX timestamps

        # Restrict only /chat/ or /api/chat/ paths (optional for scope control)
        if request.path.startswith('/chat') or request.path.startswith('/api/chat'):
            if not (allowed_start <= now <= allowed_end):
                return HttpResponseForbidden("Chat is only accessible between 6:00 PM and 9:00 PM.")

        return self.get_response(request)


# chats/middleware.py

from django.http import JsonResponse

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.message_log = {}  # Format: {ip: [(timestamp1), (timestamp2), ...]}

    def __call__(self, request):
        if request.path.startswith('/chat') and request.method == 'POST':
            ip = self.get_client_ip(request)
            current_time = time.time()

            # Clean up old entries
            self.message_log.setdefault(ip, [])
            self.message_log[ip] = [
                ts for ts in self.message_log[ip]
                if current_time - ts < 60  # Keep messages from the last 60 seconds
            ]

            if len(self.message_log[ip]) >= 5:
                return JsonResponse(
                    {"error": "Rate limit exceeded. Max 5 messages per minute."},
                    status=429
                )

            self.message_log[ip].append(current_time)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
