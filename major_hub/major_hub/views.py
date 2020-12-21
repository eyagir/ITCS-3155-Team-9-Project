from django.shortcuts import render
import webbrowser
from django import template
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from major_hub.templates.SelectedMajorGraph.MajorEconomicGraph import major_change
from major_hub.templates.SelectedMajorGraph.MajorWorkGraph import major_change



def index(request):
    return render(request, 'index.html')

def ctool(request):
    return render(request, 'ctool.html')

def hpay(request):
    return render(request, 'hpay.html')

def popular(request):
    return render(request, 'popular.html')

def major(request):
    major = request.POST.get('majordropdown', "ACCOUNTING")
    major_change(major)
    return render(request, 'major.html')

