from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    dataRegister = models.DateField(auto_now_add=True)
    stars = models.IntegerField(default=0) 
    menuSegunda = models.CharField(max_length=150,null=True, blank=True)
    menuTerca = models.CharField(max_length=150,null=True, blank=True)
    menuQuarta = models.CharField(max_length=150,null=True, blank=True)
    menuQuinta = models.CharField(max_length=150,null=True, blank=True)
    menuSexta = models.CharField(max_length=150,null=True, blank=True)

class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=50)
    dataRegister = models.DateTimeField(auto_now_add=True)
    votaingDate =  models.DateField(auto_now_add=False,null=True, blank=True)

