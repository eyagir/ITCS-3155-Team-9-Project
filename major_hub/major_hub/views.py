from django.shortcuts import render
import webbrowser
from django import template
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from major_hub.templates.SelectedMajorGraph.MajorEconomicGraph import major_economic_change
from major_hub.templates.SelectedMajorGraph.MajorWorkGraph import major_work_change
from major_hub.templates.SelectedMajorGraph.RelatedMajors import related_majors

def convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def index(request):
    return render(request, 'index.html')

def hpay(request):
    return render(request, 'hpay.html')

def popular(request):
    return render(request, 'popular.html')

def major(request):
    major = request.POST.get('majordropdown', "ACCOUNTING")
    major_economic_change(major)
    major_work_change(major)
    rm = related_majors(major)
    return render(request, 'major.html', {'related_major': rm})

