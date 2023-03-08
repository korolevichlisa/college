from django import http
from django.http import HttpResponse
from django.shortcuts import render
from testdb.models import Colleges, News

def home(request):
    return render(request, "index.html")
    # return HttpResponse('home')


def tfk(request):
    # news = News.objects.filter(id_college__name_college = 'Одеський технічний фаховий коледж').order_by('-published_date')[:3:1]  ,{'news':news}
    return render(request, "tfk.html")

def mt(request):
    return render(request, "mt.html")

def nti(request):
    return render(request, "nti.html")

def kpa(request):
    return render(request, "kpa.html")