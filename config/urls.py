from django.contrib import admin
from django.urls import path
from lunch import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #rotas primarias principais v1 =====
    path('v1/loginUser/<str:phoneUser>/<str:passwordUser>/',views.loginUser,name="loginUser"), #POST
    path('v1/listRestaurantsOfDay/',views.getListRestaurantsOfDay,name="listRestaurantsOfDay"), #GET
    path('v1/users_list/',views.getlistUsers,name="getUsersList"), #GET
    path('v1/rankingOfToday/',views.getlistRankingOfToday,name="getlistRankingOfToday"), #GET
    path('v1/winningRestaurantToDay/',views.getWinningRestaurant,name="getWinningRestaurant"), #GET
    path('v1/resetRestaurantToVoteingToday/<listRestaurantsId>/',views.resetRestaurantForVoteing,name="resetRestaurantForVoteing"), #GET
    path('v1/voting/<idRestaurant>/<idUser>/',views.setVoteing,name="setVoteing"),#PUT
]
