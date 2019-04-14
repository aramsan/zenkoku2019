from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='entryindex'),
     path('signup/', views.signup, name='signup'),
     path('signup/request/', views.signuprequest, name='signuprequest'),
     path('edit/', views.edit, name='edit'),
     path('edit/request/', views.editrequest, name='editrequest'),
     path('login/', views.login, name='login'),
     path('login/request/', views.loginrequest, name='loginrequest'),
     path('logout/', views.logout, name='logout'),
     path('comment/<int:userid>/', views.comment, name="comment"),
     path('like/<int:userid>/', views.like, name="like"),
]