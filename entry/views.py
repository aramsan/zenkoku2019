from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Entry, Comment, Like

import hashlib
import datetime

def index(request):
    entry = Entry.objects.all().order_by('-userid')
    return render(request, 'entry/index.html',{'entry_list': entry})

def signup(request):
    error = {}
    if 'error' in request.session:
        error = request.session.get('error')
        del request.session['error']
    data = {}
    if 'data' in request.session:
        data = request.session.get('data')  
        #del request.session['data']
    return render(request, 'entry/signup.html', {'error': error, 'data': data})

def signuprequest(request):
    if 'error' in request.session:   
        del request.session['error']
    username = request.POST.get('username')
    filename = save_picture_file(request.FILES['picture'])
    rawPassword = request.POST.get('password')        
    password = hashlib.sha256(rawPassword.encode('utf-8')).hexdigest()
    data = {
        "username" : username, 
        "email"    : request.POST.get('email'),
        "password" : password,
        "picture"  : filename,
        "type"     : request.POST.get('type'),
        "grade"    : request.POST.get('grade'),
        "adult"    : request.POST.get('adult'),
        "child"    : request.POST.get('child'),
        "departure": request.POST.get('departure'),
        "message"  : request.POST.get('message')
    }
    request.session['data'] = data
    if Entry.objects.filter(username=username):
        request.session['error'] = 'ID「' + username + '」はすでに使われています'
        return HttpResponseRedirect(reverse('signup'))
    else:
        creation = Entry(
            username  = username, 
            email     = data['email'],
            password  = data['password'],
            picture   = data['picture'],
            type      = data['type'],
            grade     = data['grade'],
            adult     = data['adult'],
            child     = data['child'],
            departure = data['departure'],
            message   = data['message']
        )
        creation.save()
        request.session['username'] = username
        request.session['userid'] = creation.userid
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'app/index.html')

def save_picture_file(f):
    filename = 'static/picture/' + datetime.datetime.today().strftime('%s') + f.name
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return "/" + filename