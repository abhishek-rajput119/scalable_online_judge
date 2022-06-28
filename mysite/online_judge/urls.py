from django.urls import path
from . import views

app_name = 'online_judge'
urlpatterns = [
    # /online_judge/
    path('', views.user_login, name='login'),
    # /online_judge/home
    path('home', views.home, name='home'),
    # /online_judge/problem/id
    path('problem/<int:problem_id>', views.submission, name='submission'),
    # /online_judge/signup
    path('signup', views.signup, name='signup')
]
