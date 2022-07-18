from django.urls import path
from . import views

app_name = 'online_judge'
urlpatterns = [
    # /online_judge/
    path('login', views.user_login, name='user_login'),
    # /online_judge/home
    path('home', views.home, name='home'),
    # /online_judge/problem/id
    path('problem/<int:problem_id>', views.submission, name='submission'),
    # /online_judge/signup
    path('signup', views.signup, name='signup'),
    # /online_judge/logout
    path('logout', views.user_logout, name='logout')
]
