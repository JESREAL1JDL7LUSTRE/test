from django.http import JsonResponse

def account_data(request):
    """Return user data for authenticated requests."""
    if not hasattr(request, "clerk_state") or request.clerk_state is None:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    return JsonResponse({
        "message": "Authenticated successfully",
        "user_id": request.clerk_state.payload.get("sub"),
    })
    


