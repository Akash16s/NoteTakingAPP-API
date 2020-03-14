from django.contrib import auth
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import userSerializer
from django.contrib.auth.models import User


class takeNote(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get():
        return None


class registration(APIView):
    @staticmethod
    def post(request):
        serializer = userSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            if User.objects.filter(email=request.data["email"]).exists():
                return Response({"msg": "User Already Exists"}, status=401)
            User.objects.create_user(email=request.data["email"], password=request.data["password"],
                                     username=request.data["username"])
            return Response({"msg": "User Created"}, status=200)
        return Response({"msg": "Bad Request"}, status=200)


class login(APIView):
    @staticmethod
    def post(request):
        user = auth.authenticate(username=request.data["username"], password=request.data["password"])
        if user is not None:
            tokenObj = Token.objects.get(user=user)
            return Response({"Token": tokenObj.key}, status=200)
        return Response({"Request": "Bad Request"}, status=400)
