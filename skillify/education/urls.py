from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pupil_cabinet/', views.profile_view, name='pupil_cabinet'),
    path('subjects/', views.subjects_list, name='subjects_list'),
    path('subjects/<int:subject_id>/topics/', views.topic_list, name='topic_list'),
]


