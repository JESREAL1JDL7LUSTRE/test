from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from .clerk_utils import authenticate_request

class ClerkAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"🔍 Incoming Request to {request.path}")

        # Skip authentication for Django admin
        if str(request.path).startswith('/admin'):
            return None  

        auth_result = authenticate_request(request)  # ✅ Pass the full request object

        if auth_result is None:
            print("❌ Authentication failed: No valid token.")
            return HttpResponseForbidden("Authentication failed.")

        print(f"✅ Authenticated User: {auth_result.payload}")
        request.clerk_state = auth_result  # Store authentication result
