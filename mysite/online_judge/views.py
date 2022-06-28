# Create your views here.
from django.contrib.auth import login, authenticate

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Problem
from .forms import UserForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print(user)

                problems = Problem.objects.all()
                return render(request, 'pages/home.html', {'user': user, 'problems': problems})
            else:
                return HttpResponse("Account not active")
        else:
            print("Tried login and failed")
            print("username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'pages/login.html', {})


def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)

        if registered:
            problems = Problem.objects.all()
            return render(request, 'pages/home.html', {"user": user, 'problems': problems})

    else:
        user_form = UserForm()

    return render(request, 'pages/signup.html', {"user_form": user_form})


def home(request):
    problems = Problem.objects.all()
    return render(request, 'pages/home.html', {'problems': problems})


def submission(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    return render(request, 'pages/submission.html', {'problem': problem})





