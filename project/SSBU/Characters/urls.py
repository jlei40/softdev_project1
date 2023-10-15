from django.urls import path

from . import views

app_name = "characters"

urlpatterns = [
   path("index", views.index, name="index"),
   path("cookies", views.cookies, name="cookies"),
   path("djangoforms", views.djangoforms, name="djangoforms"),
   path("nondjangoforms", views.nondjangoforms, name="nondjangoforms"),   
   path("character_info", views.character_info, name="character_info"),
   path("search", views.search, name="search"),
   path("searched",views.searched, name="searched"),
]

