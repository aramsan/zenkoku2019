from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html');

def gallery(request):
    return render(request, 'app/gallery.html');