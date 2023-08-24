from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pupil_cabinet/', views.profile_view, name='pupil_cabinet'),
    path('subjects/', views.subjects_list, name='subjects_list'),
    path('subjects/<int:subject_id>/assignments/', views.assignments_list, name='assignments_list'),
    path('teachers/', views.all_teachers, name='all_teachers'),
    path('execute_assignment/<int:assignment_id>/', views.execute_assignment, name='execute_assignment'),
    path('feedback/', views.feedback_list, name='feedback_list'),
    path('assignment/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('send_message/<int:teacher_id>/', views.send_message, name='send_message'),
    path('message_sent/', views.message_sent, name='message_sent'),
    path('schedule_json/', views.schedule_view, name='schedule_json'),






]


