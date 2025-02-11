import os
import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from clerk_backend_api import Clerk

# Initialize Clerk SDK with the secret key
clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

class ClerkAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            raise AuthenticationFailed("No valid Authorization header found.")

        token = auth_header.split("Bearer ")[-1].strip()

        try:
            # Authenticate the request using Clerk SDK
            request_state = clerk_sdk.authenticate_request(token)

            if not request_state.is_signed_in:
                raise AuthenticationFailed("Invalid or expired token.")

            # Extract user details from the token payload
            clerk_id = request_state.payload.get("sub")
            email = request_state.payload.get("email")

            if not clerk_id:
                raise AuthenticationFailed("Clerk ID is missing in token.")

            from django.contrib.auth import get_user_model
            User = get_user_model()

            # Get or create user in Django DB
            user, _ = User.objects.get_or_create(
                clerk_id=clerk_id,
                defaults={"email": email, "username": email.split("@")[0]},
            )

            return (user, None)

        except Exception as e:
            raise AuthenticationFailed(f"Authentication failed: {str(e)}")
