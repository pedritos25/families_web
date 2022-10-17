from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import families

def index(request):
    familiares = families.objects.all()
    context = {'familiares': 'listado', 'familiares': familiares}
    return render(request, 'families_list.html', context)