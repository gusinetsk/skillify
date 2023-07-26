from django.shortcuts import render, redirect
from .models import Student
from .forms import RegistrationForm

def autorization(request):
    return render(request, 'autorization.html')
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autorization')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

