from django.urls import path
from . import views

urlpatterns = [
   path("animefolio/", views.animefolio, name='animefolio'),
   
]