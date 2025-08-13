from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .form import *

# Create your views here.

def homepagefn(request):
    return render(request,'home.html')
