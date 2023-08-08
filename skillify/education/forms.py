from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, BaseUserCreationForm


class PupilAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Pupil

class CustomRegistrationForm(BaseUserCreationForm):
    sex = forms.ChoiceField(choices=SEX, label='Пол')
    photo = forms.ImageField(required=False, label='Фото')
    grade_class = forms.ModelChoiceField(queryset=GradeClass.objects.all(), label='Класс')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повторите пароль')
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email','sex', 'photo', 'grade_class','password1', 'password2')

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("Пароль должен быть не менее 8 символов")
        return password1

    def clean_password_confirmation(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2


