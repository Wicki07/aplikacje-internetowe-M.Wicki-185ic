from django.contrib.auth import get_user_model 
from rest_framework import filters
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Ksiazka

from .permissions import IsAuthorOrReadOnly
from .serializers import KsiazkaSerializer, UserSerializer
"""
class PostViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

"""    

class KsiazkaList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # View-Level Permissions
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']

class KsiazkaDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)

    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer

"""
class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
"""
