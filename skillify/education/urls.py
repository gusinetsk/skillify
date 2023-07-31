from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration, name='registration'),
    path('pupil/<int:pupil_id>/', views.pupil_cabinet, name='pupil_cabinet'),
    path('subjects/<int:pupil_id>/', views.subjects_list, name='subjects_list'),
]


