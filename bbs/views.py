from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Thread, Comment

def index(request):
    bbs_list = Thread.objects.all().order_by('-pub_date')
    comment_list = Comment.objects.all().order_by('-pub_date')
    return render(request, 'bbs/index.html', {'bbs_list':bbs_list, 'commnet_list':comment_list})

def post(request):
    creation = Thread(name=request.POST.get('name'),email=request.POST.get('email'),message=request.POST.get('message'))
    creation.save()
    return HttpResponseRedirect(reverse('bbsindex'))

def comment(request):
    thread = Thread.objects.get(id=request.POST.get('id'))
    creation = Comment(thread=thread, name=request.POST.get('comment_name'),email=request.POST.get('comment_email'),message=request.POST.get('comment_message'))
    creation.save()
    return HttpResponseRedirect(reverse('bbsindex'))