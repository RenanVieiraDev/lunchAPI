from django.contrib import admin
from lunch.models import Restaurant
from lunch.models import User

class Restaurants(admin.ModelAdmin):
    list_display = ("id","name","stars","dataRegister")
    list_display_links = ("id","name")
    search_fields = ("name",)
    readonly_fields = ("stars",)

class Users(admin.ModelAdmin):
    list_display = ("id","name",)
    list_display_links = ("id","name",)
    search_fields = ("name",)
    readonly_fields = ("votaingDate",)

admin.site.register(Restaurant,Restaurants)
admin.site.register(User,Users)

