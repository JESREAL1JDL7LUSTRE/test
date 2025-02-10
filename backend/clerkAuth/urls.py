from django.urls import path
from .views import test_auth

urlpatterns = [
    path('api/test-auth/', test_auth),
]
