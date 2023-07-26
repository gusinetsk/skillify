from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('autorization/', views.autorization, name='autorization'),
    path('register/', views.register_user, name='registration'),


]