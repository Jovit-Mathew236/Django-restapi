from django.shortcuts import render
from .serializers import UserSignUp, UserDataSerializer, LoginSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth

# Create your views here.

class signup(APIView):
    
    def post(self,request,format=None):
        serializer=UserSignUp(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='success'
        else:
            data=serializer.errors
        return Response(data)

class login(APIView):

    def get(self,format=None):
        return Response({"data":"login"})
    
    def post(self,request,format=None):
        serializer = LoginSerializers(data=request.data)
        data = {}
        if serializer.is_valid(raise_exception=True):
            data['response'] = 'success'
        else:
            data = serializer.errors
        return Response(data)    

    # def post(self, request, *args, **kwargs):
    #     serializer = LoginSerializers(data=request.data)
    #     if serializer.is_valid():
    #         name = request.POST['username']
    #         password = request.POST['password']
    #         # msg = 'Hello{}'.format(name)
    #         user = auth.authenticate(username=name, password=password)
    #         if user is not None:
    #             return Response('success')
