from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Playa

@login_required
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def lista_playas(request):
    playas = Playa.objects.all()
    return render(request, 'lista_playas.html', {'playas': playas})