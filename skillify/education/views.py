from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            pupil = form.save()
            return redirect('login')
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pupil_cabinet')
        else:
            error_message = "Неверное имя пользователя или пароль."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
@login_required
def pupil_cabinet(request):
    pupil = request.user.pupil
    return render(request, 'pupil_cabinet.html', {'pupil': pupil})
# def pupil_cabinet(request, pupil_id):
#     try:
#         pupil = Pupil.objects.get(id=pupil_id)
#         grade_achievements = GradeAchievement.objects.filter(student=pupil)
#
#         context = {
#             'pupil': pupil,
#             'grade_achievements': grade_achievements,
#         }
#         return render(request, 'pupil_cabinet.html', context)
#     except Pupil.DoesNotExist:
#         return render(request, 'error.html', {'error_message': 'Ученик не найден'})
#
# def subjects_list(request,pupil_id):
#     pupil = Pupil.objects.get(id=pupil_id)
#     class_number = pupil.grade_class.class_number
#     if class_number == '1' or class_number == '2':
#         subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'бел.лит', 'рус.лит', 'матем'])
#     if class_number == '3' or class_number == '4':
#         subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз','бел.лит','рус.лит','матем'])
#     if class_number == '5' or class_number == '6':
#         subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз', 'бел.лит', 'рус.лит', 'матем', 'ист',
#                                                     'био', 'гео', 'инф'])
#     if class_number == '7' :
#         subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз', 'бел.лит', 'рус.лит', 'матем', 'ист',
#                                                     'био', 'гео', 'инф','физ', 'хим'])
#     if class_number in ('8', '9', '10', '11'):
#         subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз', 'бел.лит', 'рус.лит', 'матем', 'ист',
#                                                     'био', 'гео', 'инф','физ','хим', 'общ'])
#     context = {
#         'pupil': pupil,
#         'subjects': subjects,
#     }
#     return render(request, 'subjects_list.html', context)
#
#
#
# def topic_list(request, subject_id):
#     subject = get_object_or_404(Subject, id=subject_id)
#     topics = Topic.objects.filter(subject=subject)
#
#     context = {
#         'subject': subject,
#         'topics': topics,
#     }
#
#     return render(request, 'topic_list.html', context)
