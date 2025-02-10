# clerkAuth/clerk_utils.py
import os
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions

# Initialize the Clerk SDK instance using the secret key from settings or environment
clerk_sdk = Clerk(bearer_auth=os.getenv('CLERK_SECRET_KEY'))


def authenticate_request(request):
    print("🔍 Incoming Headers:", request.headers)  # Debugging

    auth_header = request.headers.get('Authorization')

    if not auth_header:  # Check if the header exists
        print("❌ No Authorization header found")
        return None

    if not auth_header.startswith("Bearer "):  # Ensure it has the expected format
        print("❌ Invalid Authorization header format:", auth_header)
        return None

    token = auth_header.split("Bearer ")[-1].strip()
    print("🔑 Extracted Token:", token)  # Debugging

    try:
        request_state = clerk_sdk.authenticate_request(token)
        if request_state.is_signed_in:
            print("✅ Authentication Success:", request_state.payload)
            return request_state
    except Exception as e:
        print("❌ Clerk authentication failed:", e)

    return None

