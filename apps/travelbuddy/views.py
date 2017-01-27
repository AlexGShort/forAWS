from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):

    return render(request, 'index.html')

def new(request):

    return render(request, 'new.html')

def create(request):

    return redirect(reverse('travelbuddy:index'))

def show(request, id):

    return render(request, 'show.html')
