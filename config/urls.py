from django.contrib import admin
from django.urls import path
from lunch import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #rotas primarias principais v1 =====
    path('v1/loginUser/<str:phoneUser>/<str:passwordUser>/',views.loginUser,name="loginUser"), #POST
    path('v1/listRestaurants/',views.getListRestaurants,name="listRestaurants"), #GET
    path('v1/users_list/',views.getlistUsers,name="getUsersList"), #GET
    path('v1/voting/<idRestaurant>/<idUser>/',views.setVoteing,name="setVoteing"),#PUT
]
