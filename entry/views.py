from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum
from .models import Entry, Comment, Like

import hashlib
import datetime

def index(request):
    entry = Entry.objects.all().order_by('-userid')
    stat = entry.aggregate(Sum('adult'), Sum('child'), Sum('after_adult'), Sum('after_child'))
    return render(request, 'entry/index.html',{'entry_list': entry, 'stat': stat})

def signup(request):
    error = {}
    if 'error' in request.session:
        error = request.session.get('error')
        del request.session['error']
    data = {}
    if 'data' in request.session:
        data = request.session.get('data')  
        del request.session['data']
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
        "after_adult" : request.POST.get('after_adult'),
        "after_child" : request.POST.get('after_child'),
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
            after_adult = data['after_adult'],
            after_child = data['after_child'],
            departure = data['departure'],
            message   = data['message']
        )
        creation.save()
        request.session['username'] = username
        request.session['userid'] = creation.userid
        request.session['email'] = creation.email
        del request.session['data']
        return HttpResponseRedirect(reverse('entryindex'))

    return render(request, 'app/index.html')

def edit(request):
    error = {}
    if 'error' in request.session:
        error = request.session.get('error')
        del request.session['error']
    data = Entry.objects.filter(userid=request.session['userid']).first()
    if 'data' in request.session:
        data = request.session.get('data')  
        del request.session['data']
    return render(request, 'entry/edit.html', {'error': error, 'data': data})

def editrequest(request):
    if 'error' in request.session:   
        del request.session['error']
    username = request.POST.get('username')
    filename = ''
    if 'picture' in request.FILES:
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
        "after_adult" : request.POST.get('after_adult'),
        "after_child" : request.POST.get('after_child'),
        "departure": request.POST.get('departure'),
        "message"  : request.POST.get('message')
    }
    request.session['data'] = data
    update = Entry.objects.filter(userid=request.session['userid']).first()
    update.userid    = request.session['userid']
    update.username  = username
    update.email     = data['email']
    update.password  = data['password']
    update.type      = data['type']
    update.grade     = data['grade']
    update.adult     = data['adult']
    update.child     = data['child']
    update.after_adult = data['after_adult']
    update.after_child = data['after_child']
    update.departure = data['departure']
    update.message   = data['message']
    if data['picture']:
        update.picture = data['picture']
    update.save()
    request.session['username'] = username
    request.session['userid'] = update.userid
    request.session['email'] = update.email
    del request.session['data']
    return HttpResponseRedirect(reverse('entryindex') + "#" + str(request.session['userid']))

def login(request):
    return render(request, 'entry/login.html')

def loginrequest(request):
    error = ''
    email = request.POST.get('email')
    rawPassword = request.POST.get('password')
    password = hashlib.sha256(rawPassword.encode('utf-8')).hexdigest()
    entry = Entry.objects.filter(email=email, password=password).first()
    if entry:
        request.session['username'] = entry.username
        request.session['userid'] = entry.userid
        request.session['email'] = entry.email
        request.session['is_admin'] = entry.is_admin
        return HttpResponseRedirect(reverse('index'))
    else:
        error='メールアドレス、または、パスワードが間違っています'
        return render(request, 'entry/login.html',{'error': error, 'email': email})

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    if 'userid' in request.session:
        del request.session['userid']
    return HttpResponseRedirect(reverse('index'))

def comment(request, userid):
    entry = Entry.objects.filter(userid=userid).first()
    commenterid = request.session['userid']
    commenter = Entry.objects.filter(userid=commenterid).first()
    creation = Comment(
        userid = entry,
        commenter = commenterid,
        message = request.POST.get('comment')
    )
    creation.save()
    return HttpResponseRedirect(reverse('entryindex') + "#" + str(userid))

def like(request, userid):
    entry = Entry.objects.filter(userid=userid).first()
    likerid = request.session['userid']
    likecheck = Like.objects.filter(userid=userid, liker=likerid).first()
    if likecheck:
        likecheck.delete()
    else:
        liker = Entry.objects.filter(userid=likerid).first()
        creation = Like(
            userid = entry,
            liker = likerid,
        )
        creation.save()

    return HttpResponseRedirect(reverse('entryindex') + "#" + str(userid))

def admin(request):
    if 'userid' in request.session:
        admin = Entry.objects.filter(userid=request.session['userid']).first()
        if admin.is_admin:
            entry = Entry.objects.all().order_by('-userid')
            stat = entry.aggregate(Sum('adult'), Sum('child'), Sum('after_adult'), Sum('after_child'))
            stat_type = {
                "soarer10" :  Entry.objects.filter(type='10ソアラ').count(),
                "soarer20" :  Entry.objects.filter(type='20ソアラ').count(),
                "soarer30" :  Entry.objects.filter(type='30ソアラ').count(),
                "soarer40" :  Entry.objects.filter(type='40ソアラ').count(),
                "other"    :  Entry.objects.filter(type='その他').count(),
            }
            return render(request, 'entry/admin.html',{'entry_list': entry, 'stat': stat, 'stat_type': stat_type})
        else:
            return HttpResponseRedirect(reverse('index'))    
    else:
        return HttpResponseRedirect(reverse('index'))


def save_picture_file(f):
    filename = 'static/picture/' + datetime.datetime.today().strftime('%s') + f.name
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return "/" + filename