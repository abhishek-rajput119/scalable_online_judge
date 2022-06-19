from django.urls import path
from . import views

app_name = 'online_judge'
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name = 'home'),
    path('submission',views.submission,name='submission')
]