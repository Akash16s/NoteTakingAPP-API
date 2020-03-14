from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import userSerializer, noteSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from .models import noteModel
from datetime import datetime
import django_filters.rest_framework


class getNote(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = noteModel.objects.all()
    serializer_class = noteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'newUpdatedDate', 'lastUpdatedDate']


class takeNote(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = noteSerializer(data=request.data, many=False, partial=True)
        if serializer.is_valid():
            noteModel.objects.create(
                user=request.user,
                note=request.data["note"],
                newUpdatedDate=datetime.today(),
                lastUpdatedDate=datetime.today()
            ).save()
            return Response({"msg": "Data Saved"}, status=200)
        return Response({"msg": "Bad Request"}, status=400)

    @staticmethod
    def put(request):
        serializer = noteSerializer(data=request.data, partial=True, many=False)
        if serializer.is_valid():
            try:
                note = noteModel.objects.get(id=request.data["id"])
            except ObjectDoesNotExist:
                return Response({"msg": "Not Found"}, status=404)
            note.note = request.data["note"]
            note.lastUpdatedDate = note.newUpdatedDate
            note.newUpdatedDate = datetime.today()
            note.save()
            return Response({"msg": "Saved the changes"}, status=200)
        return Response({"msg": "Bad Request"}, status=400)


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
