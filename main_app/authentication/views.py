from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from rest_framework.exceptions import AuthenticationFailed
# Create your views here.


class RegisterView(APIView):

    def post(self, request):
        single_user = request.data.get('users')
        serializer = UserSerializer(data=single_user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.name)})


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        return Response({"success": 'User logs in!'})
