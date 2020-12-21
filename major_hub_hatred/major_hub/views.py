from django.shortcuts import render
import webbrowser
from django import template

def index(request):
    return render(request, 'index.html')

def ctool(request):
    return render(request, 'ctool.html')

def hpay(request):
    return render(request, 'hpay.html')

def popular(request):
    return render(request, 'popular.html')

def major(request):
    return render(request, 'major.html')
