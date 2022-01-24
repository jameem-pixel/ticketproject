
from .models import *
# Create your views here.
from django.shortcuts import render,redirect
from .models import *
def home(request):
    return render(request,'task/home.html')
