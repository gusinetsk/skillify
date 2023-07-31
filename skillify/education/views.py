from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pupil_cabinet.html')
            else:
                print('Данные не верны')
                messages.add_message(request, messages.ERROR,
                                     'Неправильный логин или пароль. Пожалуйста, попробуйте снова.')
                messages.info(request, 'Это временное сообщение для проверки')
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def pupil_cabinet(request, pupil_id):
    try:
        pupil = Pupil.objects.get(id=pupil_id)
        grade_achievements = GradeAchievement.objects.filter(student=pupil)

        context = {
            'pupil': pupil,
            'grade_achievements': grade_achievements,
        }
        return render(request, 'pupil_cabinet.html', context)
    except Pupil.DoesNotExist:
        return render(request, 'error.html', {'error_message': 'Ученик не найден'})

def subjects_list(request,pupil_id):
    pupil = Pupil.objects.get(id=pupil_id)
    class_number = pupil.grade_class.class_number
    if class_number == '1' or class_number == '2':
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'бел.лит', 'рус.лит', 'матем'])
    if class_number == '3' or class_number == '4':
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз','бел.лит','рус.лит','матем'])
    if class_number == '5' or class_number == '6':
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз', 'бел.лит', 'рус.лит', 'матем', 'ист',
                                                    'био', 'гео', 'инф'])
    if class_number == '7' :
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз', 'бел.лит', 'рус.лит', 'матем', 'ист',
                                                    'био', 'гео', 'инф','физ', 'хим'])
    if class_number in ('8', '9', '10', '11'):
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз', 'бел.лит', 'рус.лит', 'матем', 'ист',
                                                    'био', 'гео', 'инф','физ','хим', 'общ'])
    context = {
        'pupil': pupil,
        'subjects': subjects,
    }
    return render(request, 'subjects_list.html', context)


