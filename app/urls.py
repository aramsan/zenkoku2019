from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('gallery', views.gallery, name='gallery'),
     path('threemonth', views.threemonth, name='threemonth'),
     path('lunch', views.lunch, name='lunch'),
]