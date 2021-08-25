from django.db.models.base import Model
from rest_framework import serializers
from lunch.models import Restaurant,User

class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
      model = Restaurant
      fields = ('id','name','dataRegister','stars','menuSegunda','menuTerca','menuQuarta','menuQuinta','menuSexta')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('id','name','phone','dataRegister')