from django.urls import path

from . import views

urlpatterns = [
     path('', views.index, name='bbsindex'),
     path('post/', views.post, name='bbspost'),
     path('comment/', views.comment, name='bbscomment'),
]