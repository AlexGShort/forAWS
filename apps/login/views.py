from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
# from django import forms
from .forms import RegistrationForm, LoginForm
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def login(request):
    if request.method=='POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            response = User.objects.filter(username = request.POST['username'])
            request.session['user_name'] = response[0].username
            request.session['user_id'] = response[0].id
            # print "#"*50
            # print "request session username: {}, id: {}".format(request.session['username'], request.session['id'])
            return redirect(reverse('travelbuddy:index'))
        else:
            registrationForm = RegistrationForm()
            context = {'loginForm': loginForm, 'registrationForm': registrationForm}
            return render(request, 'login/login.html', context)
    else:
        loginForm = LoginForm()
        registrationForm = RegistrationForm()
        context = {"loginForm": loginForm, "registrationForm": registrationForm}
        return render(request, 'login/login.html', context)

def registration(request):
    if request.method=='POST':
        registrationForm = RegistrationForm(request.POST)
        loginForm = LoginForm()
        if registrationForm.is_valid():
            newUser = registrationForm.save()
            request.session['user_name'] = newUser.username
            request.session['user_id'] = newUser.id
            return redirect(reverse('travelbuddy:index'))
    else:
        registrationForm = RegistrationForm()
        loginForm = LoginForm()

    context = {"registrationForm": registrationForm, "loginForm": loginForm}
    return render(request, 'login/login.html', context)

def logout(request):
    request.session.flush()
    return redirect(reverse('login:login'))

def success(request):

    return render(request, 'login/success.html')
