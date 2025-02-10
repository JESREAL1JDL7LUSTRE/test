from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test_auth(request):
    auth_header = request.headers.get('Authorization')
    
    if not auth_header:
        return JsonResponse({"error": "No Authorization header"}, status=403)

    token = auth_header.split("Bearer ")[-1].strip()

    import jwt
    decoded = jwt.decode(token, options={"verify_signature": False})  # Only for testing!
    
    return JsonResponse({"message": "Authenticated!", "decoded": decoded})
