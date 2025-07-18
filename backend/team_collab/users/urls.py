from django.urls import path
from .views import UserRegister

urlpatterns = [
    path('api/register/', UserRegister.as_view())
]