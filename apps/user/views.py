from rest_framework import generics, permissions

from .models import User
from .serializers import SignUpSerializer


class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SignUpSerializer
