# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'pages/login.html')


def home(request):
    return render(request, 'pages/home.html')


def submission(request):
    return render(request, 'pages/submission.html')


def signup(request):
    return render(request, 'pages/signup.html')
