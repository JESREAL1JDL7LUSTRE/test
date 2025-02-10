from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class ClerkAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # TODO: Implement actual Clerk authentication logic
        return None
