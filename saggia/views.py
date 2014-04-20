from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth import *
from saggia.models import *

############# DETAIL PAGES 

def index(request):
    context={}
    profiles = list()
    profiles.append(Profile(user = request.user))
    context['profiles'] = profiles
    return addMenu(request, 'index.html', context)
    
def user(request, uname=""):
    if uname=="":
        uname = request.user.username    
    context={}
    uname = uname+""
    uuser = User.objects.filter(username = uname)
    profile = Profile.objects.get(user = uuser)
    context['p'] = profile
    context['r'] = request.user
    return addMenu(request, 'user.html', context)

def appointment(request, code=-1):
    context={}
    return addMenu(request, 'detail.html', context)
########## SPECIAL PAGES
    
def first(request):
    context={}
    form = AuthenticationForm()
    context['form'] = form
    return render(request, 'first.html', context)

def error(request):
    context={}
    return render(request, 'error.html', context)


########## ACTION PAGES

def invite(request):
    return redirect('/appointment')
    
    
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/index')
        else:
            return redirect('/error')
    else:
        return redirect('/error')


def logout_view(request):
    logout(request)
    return redirect('/')

def addMenu(request, template='base.html', context={}):
    context ['menuelements'] = MenuElement.objects.all
    return render(request, template, context)
    
