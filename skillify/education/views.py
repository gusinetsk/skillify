from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
import json
from django.http import JsonResponse
from pprint import pprint


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.photo = request.FILES.get('photo')
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.sex = form.cleaned_data['sex']
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
    subjects = Subject.objects.filter(grade_class=user.grade_class)

    achievements = []
    for subject in subjects:
        average_grade = GradeAchievement.objects.filter(user=user, subject=subject).aggregate(Avg('total_grade'))[
            'total_grade__avg']
        achievements.append({'subject': subject, 'average_grade': average_grade})

    context = {
        'user': user,
        'achievements': achievements,
    }
    return render(request, 'pupil_cabinet.html', context)

def subjects_list(request):
    user = request.user
    class_number = user.grade_class.class_number
    if class_number == '1' or class_number == '2':
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'бел.лит', 'рус.лит', 'матем'])
    if class_number == '3' or class_number == '4':
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз','бел.лит','рус.лит','матем'])
    if class_number == '5' or class_number == '6':
        subjects = Subject.objects.filter(name__in=['бел.яз', 'рус.яз', 'англ.яз', 'бел.лит', 'рус.лит', 'матем', 'ист',
                                                    'био', 'гео'])
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



# views.py
def execute_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)

    if request.method == 'POST':
        answer = request.POST.get('answer')
        file = request.FILES.get('file')
        image = request.FILES.get('image')

        submission = StudentSubmission.objects.create(
            student=request.user,
            answer=answer,
            file=file,
            image=image
        )

        submission.assignments.add(assignment)  # Привязываем отправку к заданию

        return redirect('assignment_detail', assignment_id=assignment_id)

    context = {
        'assignment': assignment
    }
    return render(request, 'execute_assignment.html', context)

def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    submissions = StudentSubmission.objects.filter(assignments=assignment)
    student = request.user
    context = {
        'user': student,
        'assignment': assignment,
        'submissions': submissions,
    }

    return render(request, 'assignment_detail.html', context)




def all_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

# def write_to_teacher(request, teacher_id):
#     teacher = Teacher.objects.get(id=teacher_id)
#     return render(request, 'write_to_teacher.html', {'teacher': teacher})


@login_required
def feedback_list(request):
    user = request.user
    feedbacks = Feedback.objects.filter(user=user)

    context = {
        'user': user,
        'feedbacks': feedbacks,
    }
    return render(request, 'feedback_list.html', context)



def send_message(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        form = StudentMessageForm(request.POST)
        if form.is_valid():
            sender_student = request.user
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            StudentMessage.objects.create(sender=sender_student, teacher=teacher, subject=subject, message=message)
            return redirect('message_sent')
    else:
        form = StudentMessageForm()

    return render(request, 'send_message.html', {'form': form})




def message_sent(request):
    return render(request, 'message_sent.html')


import json
from django.shortcuts import render



def schedule_view(request):
    with open('schedule_data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        schedule = data.get('5', [])

    return render(request, 'schedule_json.html', {'schedule': schedule})





