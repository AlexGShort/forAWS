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
            response = User.objects.filter(email = request.POST['email'])
            request.session['user_name'] = response[0].first_name
            request.session['user_id'] = response[0].id
            return render(request, 'login/success.html', context = {'logOrReg': 'logged in'})
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
            request.session['user_name'] = newUser.first_name
            request.session['user_id'] = newUser.id
            context = {'user_name': newUser.first_name, 'logOrReg': 'registered'}
            return render(request, 'login/success.html', context)
    else:
        registrationForm = RegistrationForm()
        loginForm = LoginForm()

    context = {"registrationForm": registrationForm, "loginForm": loginForm}
    return render(request, 'login/login.html', context)



def success(request):

    return render(request, 'login/success.html')
