from appImdbTutorial.models import Film
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = User
        fields = ['id', 'username', 'email']

class FilmSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = Film
        fields = ['id', 'title', 'year', 'description', 'release']