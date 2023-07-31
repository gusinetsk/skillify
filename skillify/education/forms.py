from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput,label='Повторите пароль')
    grade_class = forms.ModelChoiceField(queryset=GradeClass.objects.all(), label='Класс')
    class Meta:
        model = Pupil
        fields = ('name', 'surname', 'sex', 'email', 'grade_class', 'username','password', 'password_confirmation','photo')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Пароль должен быть не менее 8 символов")
        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password and password_confirmation and password != password_confirmation:
            raise ValidationError("Пароли не совпадают")
        return password_confirmation


