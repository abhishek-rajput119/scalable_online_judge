# Create your views here.
import os

from django.contrib.auth import login, authenticate, logout

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import subprocess
from .models import Problem
from .forms import UserForm


def user_logout(request):
    # del request.session['user_id']
    request.session.flush()
    logout(request)
    return user_login(request)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

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
    compiled = False
    code_text = ""
    if request.method == "POST":
        verdict = False
        compiled = True
        user = request.user
        code_text = request.POST['code']

        f = open(f"codes/{user.id}_{problem_id}.cpp", "w")
        f.write(code_text)
        f.close()

        f = open(f"codes/inputs/{problem_id}.txt", 'r')
        input_text = f.read()
        f.close()

        coded_input_text = []
        with open(f"codes/inputs/{problem_id}.txt") as f:
            coded_input_text = [x.rstrip() for x in f]

        print(coded_input_text)
        f = open(f"codes/outputs/{problem_id}.txt", "r")
        expected_output = f.read().strip()

        # subprocess.run(['docker', 'ps'])
        subprocess.run(['docker', 'cp', f'codes/{user.id}_{problem_id}.cpp', '764361bc5ec4:/a.cpp'], shell=True,
                       capture_output=True)
        output = subprocess.run(['docker', 'exec', '764361bc5ec4', 'g++', 'a.cpp'], shell=True,
                                capture_output=True, text=True)

        print(output.stderr)
        if output.returncode == 0:
            out = subprocess.run(['docker', 'exec', '-i', '764361bc5ec4', './a.out'], shell=True, capture_output=True,
                                 text=True, input=input_text)
            print(out)
            subprocess.run(['docker', 'exec', '764361bc5ec4', 'rm', '-rf', 'a.out'], shell=True)
            subprocess.run(['docker', 'exec', '764361bc5ec4', 'rm', '-rf', 'a.cpp'], shell=True)

            with open(f"codes/outputs/{user.id}_{problem_id}.txt", "w") as f:
                f.write(out.stdout)

            with open(f"codes/outputs/{user.id}_{problem_id}.txt", "r") as f:
                your_output = f.read().strip()

            if os.path.exists(f"codes/outputs/{user.id}_{problem_id}.txt"):
                os.remove(f"codes/outputs/{user.id}_{problem_id}.txt")
            else:
                print("The file does not exist")

            if os.path.exists(f"codes/{user.id}_{problem_id}.cpp"):
                os.remove(f"codes/{user.id}_{problem_id}.cpp")
            else:
                print("The file does not exist")

            print(input_text)
            print(expected_output)
            print(your_output)

            if len(your_output) != len(expected_output):
                print("length are not equal")
            else:
                for i in range(len(your_output)):
                    if your_output[i] != expected_output[i]:
                        print("Character mismatch")

            verdict = (your_output == expected_output)
            print(verdict)

            return render(request, 'pages/submission.html', {'problem': problem,
                                                             'compiled': compiled,
                                                             'input_text': coded_input_text,
                                                             'return_code': output.returncode,
                                                             'expected_output': expected_output,
                                                             'your_output': your_output,
                                                             'verdict': verdict,
                                                             'code_text': code_text
                                                             })
        return render(request, 'pages/submission.html', {'problem': problem,
                                                         'compiled': compiled,
                                                         'input_text': coded_input_text,
                                                         'return_code': output.returncode,
                                                         'expected_output': expected_output,
                                                         'error_message': output.stderr,
                                                         'code_text': code_text
                                                         })

    return render(request, 'pages/submission.html', {'problem': problem, 'compiled': compiled,
                                                     'code_text': code_text})
