from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = User
        fields = ['username', 'email']