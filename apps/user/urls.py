from django.urls import path
from .views import CreateUserAPIView, VerifyAPIView, GetNewVerification, ChangeUserInformationView, ChangeUserPhotoView

urlpatterns = [
    path("signup/", CreateUserAPIView.as_view(), name="signup"),
    path("verify/", VerifyAPIView.as_view(), name="verify"),
    path("new-verify/", GetNewVerification.as_view(), name="new-verify"),
    path('change-user/', ChangeUserInformationView.as_view(), name="change-user"),
    path('change-user-photo/', ChangeUserPhotoView.as_view(), name="change-user-photo"),
]
