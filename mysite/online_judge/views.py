# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("First Step.")


def home(request):
    return render(request,'pages/home.html')

def submission(request):
    return render(request,'pages/submission.html')