from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Ksiazka


class KsiazkaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'description', 'created_at',)
        model = Ksiazka


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
