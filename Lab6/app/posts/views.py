from django.contrib.auth import get_user_model 
from rest_framework import filters
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics, permissions
from .models import Post

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import HTMLFormRenderer,JSONRenderer,BrowsableAPIRenderer 
import datetime
from django.utils.timezone import now
"""
class PostViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

"""    

class PostList(APIView):
    serializer_class = PostSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    # definujemy funkcję post ponieważ odpowiada za formularz dodawania nowych postów
    def post(self, request, *args, **kwargs):
    
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # definujemy funkcję get ponieważ odpowiada ona za wyświetlanie postó na stronie
    def get(self, request, *args, **kwargs):
        snippets = Post.objects.all()
        serializer = PostSerializer(snippets,many=True)  
        #Tworzenie obiektu klasy response przy pomocy danych serializera
        response =  Response(serializer.data)
        # pobieranie ilość "odwiedzin" z cookies jeśli nie ma ustaw na 0
        value =int(request.COOKIES.get('visits', '0'))
        # jeżeli cookis visits istnie to if się wykona
        if request.COOKIES.get('visits' ):
            # ustawienie odpowiednich wartosci do cookies
                response.set_cookie('visits', value + 1 )
                response.set_cookie('last_visit', 'Witaj poraz kolejny')
        else:
            # ustawienie odpowiednich wartosci do cookies
                response.set_cookie('last_visit', 'Witaj poraz pierwszy' )
                response.set_cookie('visits', value + 1 )
        return response

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (IsAuthorOrReadOnly,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
