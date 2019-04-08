from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='entryindex'),
     path('signup/', views.signup, name='signup'),
     path('signup/request/', views.signuprequest, name='signuprequest'),
]