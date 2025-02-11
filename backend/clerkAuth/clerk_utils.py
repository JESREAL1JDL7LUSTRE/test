import os
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions

# Initialize Clerk SDK
clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

def authenticate_request(request):
    """Authenticate a request using Clerk."""
    print("🔍 Incoming Request:", request)

    auth_header = request.headers.get("Authorization")  # ✅ Get header from request object

    if not auth_header or not auth_header.startswith("Bearer "):
        print("❌ Invalid or missing Authorization header")
        return None

    token = auth_header.split("Bearer ")[-1].strip()
    print("🔑 Extracted Token:", token)

    # Use AuthenticateRequestOptions
    options = AuthenticateRequestOptions(
        authorized_parties=["http://localhost:5173"]
    )

    try:
        # ✅ Pass the full request object, NOT just the token
        request_state = clerk_sdk.authenticate_request(request, options)

        if request_state.is_signed_in:
            print("✅ Authentication Success:", request_state.payload)
            return request_state

        else:
            print("❌ User is not signed in.")

    except Exception as e:
        print(f"❌ Clerk authentication failed: {e}")

    return None
