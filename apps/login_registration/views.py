from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from models import *

# Create your views here.

def index(request):
    return render(request, 'login_registration/index.html')

def success(request):
    return render(request, 'login_registration/success.html')

def create(request):
    if request.method != "POST":
        return redirect('/')
    errors = User.objects.reg_validator(request.POST)
    if len(errors):
        for tag, error, in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            print messages
        return redirect('/')
    else:
        return redirect('/success')

def login(request):
    if request.method != "POST":
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error, in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        return redirect('/success')
