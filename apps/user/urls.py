from django.urls import path
from .views import CreateUserAPIView

urlpatterns = [
    path("signup/", CreateUserAPIView.as_view(), name="signup")
]
