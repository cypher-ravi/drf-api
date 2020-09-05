from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User,Group

#third party imports
from rest_framework import mixins,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics

#importing serializers
from .serializers import PostSerializer,UserSerializer,GroupSerializer
from .models import Post

class UserViewset(viewsets.ModelViewSet):
    """

    API endpoint that allow users to be viewed or edited
    
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    """

    API endpoint that allowed groups to viewed and edited.

    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

