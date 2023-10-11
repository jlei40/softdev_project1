from django.urls import path

from . import views

app_name = "characters"

urlpatterns = [
   path("", views.index, name="index"),
   # path("cookies", views.cookies, name="cookies"),
   # path("djangoforms", views.djangoforms, name="djangoforms"),
   # path("nondjangoforms", views.nondjangoforms, name="nondjangoforms"),   
]

