from datetime import date,datetime
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse, request, response
from .models import Restaurant,User
from django.core import serializers

#funções de capituras das rotas GET,POST,PUT,DELETE
def loginUser(request,phoneUser,passwordUser):
    user = User.objects.filter(phone=phoneUser,password=passwordUser)
    if request.method == 'POST':
      if(user): return HttpResponse(serializers.serialize("json",user))
      return JsonResponse({'error':'Usuario invalido','code':'01','rigthMethod':request.method})
    return JsonResponse({'error':'method invalido','code':'00','rigthMethod':'POST'})

def getListRestaurants(request):
  if request.method == 'GET':
   return HttpResponse(serializers.serialize("json", Restaurant.objects.filter(dataRegister=date.today())))
  return JsonResponse({'error':'method invalido','code':'00','rigthMethod':'GET'})

def getlistUsers(request):
  if request.method == 'GET':
    return HttpResponse(serializers.serialize("json", User.objects.all()))
  return JsonResponse({'error':'method invalido','code':'00','rigthMethod':'GET'})

def setVoteing(request,idRestaurant,idUser):
  if request.method == 'GET':
    if  validateEndHourVoteing() == False: return JsonResponse({'error':'Horario de votação encerrado!','code':'02','rigthMethod':request.method})
    if  validateInitHourVoteing() == False: return JsonResponse({'error':'Votação não iniciada!','code':'03','rigthMethod':request.method})
    if  validatePristineVoteingUser(idUser) == False: return JsonResponse({'error':'Usuario já voto hoje!','code':'04','rigthMethod':request.method})
    setVotoIncrementeRestaurant(idRestaurant,idUser)
    return HttpResponse(setNotPristineInUser(idUser))
  return JsonResponse({'error':'method invalido','code':'00','rigthMethod':'PUT'})


#Funções auxiliares para validação de horario de votação e teste de votação unica
def validateEndHourVoteing():
  if datetime.now().strftime('%H:%M:%S') > datetime.now().strftime('11:50:00'): return False
  return True

def validateInitHourVoteing():
  if datetime.now().strftime('%H:%M:%S') < datetime.now().strftime('09:00:00'): return False
  return True

def validatePristineVoteingUser(idUser):
  user = User.objects.filter(id=idUser) 
  if(user[0].votaingDate is None): 
    return True
  else:
    if(datetime.now().strftime('%D/%m/%Y') == datetime.now().strftime(format(user[0].votaingDate, "%D/%m/%Y"))):return False
  return True

#funções set's, updates e incrementos no banco de dados
def setVotoIncrementeRestaurant(idRestaurant,idUser):
  restaurant = Restaurant.objects.filter(id=idRestaurant)
  if(restaurant):
    return Restaurant.objects.filter(id=idRestaurant).update(stars = restaurant[0].stars + 1)

def setNotPristineInUser(idUser):
  return User.objects.filter(id=idUser).update(votaingDate = date.today())
   
   

  
