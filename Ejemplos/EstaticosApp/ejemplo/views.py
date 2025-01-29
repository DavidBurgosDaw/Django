from django.shortcuts import render
from pathlib import Path


def home(request):
    
# Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    return render(request,'home.html')