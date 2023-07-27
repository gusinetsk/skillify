from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('login/', views.login_view, name='login'),
    path('main/', views.autorization, name='main'),
    path('registration/', views.registration, name='registration'),


]