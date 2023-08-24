from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, BaseUserCreationForm, UserCreationForm



class CustomRegistrationForm(UserCreationForm):
    grade_class = forms.ModelChoiceField(queryset=GradeClass.objects.all())
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name','last_name',
                                                 'email','grade_class','sex','photo')

class PupilAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User


class StudentMessageForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Тема')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')





