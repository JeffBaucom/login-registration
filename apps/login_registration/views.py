from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from models import *

#GET ROUTES
#--------------------------------------------------------------------
def index(request):
    return render(request, 'login_registration/index.html')

def success(request):
    # if 'user_id' ...
    return render(request, 'login_registration/success.html')

#POST ROUTES
#--------------------------------------------------------------------
def logout(request):
    request.session.clear()
    return redirect('/')

def create(request):
    if request.method != "POST":
        return redirect('/')

    result = User.objects.reg_validator(request.POST)
    if isinstance(result, User):
        request.session['id'] = result.id
        request.session['name'] = result.first_name + " " + result.last_name
        return redirect('/success')
    else:
        for tag, error, in result.iteritems():
            messages.error(request, error, extra_tags=tag)
            print messages
        return redirect('/')

def login(request):
    if request.method != "POST":
        return redirect('/')

    result = User.objects.login_validator(request.POST)
    if isinstance(result, User):
        request.session['id'] = resut.id
        request.session['name'] = result.first_name + " " + result.last_name
        return redirect('/success')
    else:
        for tag, error, in result.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')       
