from django.core.checks import messages
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    request.session.flush()
    return render(request, "index.html")

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt(7)).decode()
    #create new user
    new_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_pw,
    )
    #store user in request.session
    request.session['user_id']= new_user.id
    return redirect('/books')

def login(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    this_user = User.objects.filter(email = request.POST['email'])[0]
    request.session['user_id'] = this_user.id
    messages.success(request, "You've successfully registered or logged in!")
    return redirect('/books')

def logout(request):
    request.session.flush()
    return redirect('/')