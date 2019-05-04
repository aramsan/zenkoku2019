from django.shortcuts import render
from entry.models import Entry

def index(request):
    if 'userid' in request.session:
        entry = Entry.objects.filter(userid=request.session['userid']).first()
        if entry.is_admin:
            request.session['is_admin'] = entry.is_admin
    return render(request, 'app/index.html')

def gallery(request):
    return render(request, 'app/gallery.html')

def threemonth(request):
    return render(request, 'app/threemonth.html')

def lunch(request):
    return render(request, 'app/lunch.html')