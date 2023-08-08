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
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            pupil = Pupil.objects.create(
                user=user,
                sex=form.cleaned_data['sex'],
                photo=form.cleaned_data['photo'],
                grade_class=form.cleaned_data['grade_class']
            )

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
def profile_view(request):
    try:
        pupil = request.user.pupil
    except Pupil.DoesNotExist:
        pupil = None

    return render(request, 'pupil_cabinet.html', {'pupil': pupil})

def subjects_list(request):
    pupil = Pupil.objects.all
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


def topic_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    topics = Topic.objects.filter(subject=subject)

    context = {
        'subject': subject,
        'topics': topics,
    }

    return render(request, 'topic_list.html', context)
