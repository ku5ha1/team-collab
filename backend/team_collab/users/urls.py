from django.urls import path
from .views import UserRegister
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/register/', UserRegister.as_view()),
    path('api/login/', obtain_auth_token, name='api_token_auth')
]