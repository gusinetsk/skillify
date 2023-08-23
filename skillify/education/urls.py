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
    path('write_to_teacher/<int:teacher_id>/', views.write_to_teacher, name='write_to_teacher'),
    # path('execute_assignment/<int:assignment_id>/', views.execute_assignment, name='execute_assignment'),


]


