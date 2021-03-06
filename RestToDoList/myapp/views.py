from django.shortcuts import render
from .models import Todolist, User
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from .serializers import TodolistSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.authentication import TokenAuthentication


# Create your views here.

class TodolistViewset(viewsets.ModelViewSet):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
