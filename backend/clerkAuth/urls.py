from django.urls import path
from .views import account_data

urlpatterns = [
    path('account-data/', account_data, name="account-data"),
]
