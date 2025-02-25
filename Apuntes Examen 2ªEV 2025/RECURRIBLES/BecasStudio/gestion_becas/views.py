from django.shortcuts import render, redirect
from .models import BecaFP, Usuario


def index(request):
    return render(request, 'index.html')

