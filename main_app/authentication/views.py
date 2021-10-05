from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


class CustomUserView(ListAPIView, CreateAPIView):

    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    # def get(self, request):
    #     return Response ({User.objects.all()
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    def post(self, request):
        user_data = request.data
        serializer = CustomUserSerializer(data=user_data)
        if serializer.is_valid(raise_exception=True):
            user_data_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(
            user_data_saved.username)})


class BlacklistTokenUpdateView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
