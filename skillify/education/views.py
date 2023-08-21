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
            user = form.save()
            user.photo = request.FILES.get('photo')
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.grade_class = form.cleaned_data['grade_class']
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('login')
    else:
        form = CustomRegistrationForm()

    return render(request, 'registration/registration.html', {'form': form})


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
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'pupil_cabinet.html', {'user': user})


def subjects_list(request):
    user = request.user
    class_number = user.grade_class.class_number
    if class_number == '1' or class_number == '2':
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'бел.лит', 'рус.лит', 'матем'])
    if class_number == '3' or class_number == '4':
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз','бел.лит','рус.лит','матем'])
    if class_number == '5' or class_number == '6':
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз', 'бел.лит', 'рус.лит', 'матем', 'ист',
                                                    'био', 'гео', 'инф'])
    if class_number == '7' or class_number == '8':
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз', 'бел.лит', 'рус.лит', 'матем', 'ист',
                                                    'био', 'гео', 'инф','физ', 'хим'])
    if class_number in ('9', '10', '11'):
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз', 'бел.лит', 'рус.лит', 'матем', 'ист',
                                                    'био', 'гео', 'инф','физ','хим', 'общ'])
    context = {
        'user': user,
        'subjects': subjects,
    }
    return render(request, 'subjects_list.html', context)


def assignments_list(request, subject_id):
    user = request.user
    subject = get_object_or_404(Subject, pk=subject_id)
    assignments = Assignment.objects.filter(subject=subject, grade_class=user.grade_class)
    return render(request, 'assignments_list.html', {'user': user, 'subject': subject, 'assignments': assignments})

def all_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def write_to_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    return render(request, 'write_to_teacher.html', {'teacher': teacher})