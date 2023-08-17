from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, BaseUserCreationForm, UserCreationForm


class PupilAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User


class CustomRegistrationForm(UserCreationForm):
    grade_class = forms.ModelChoiceField(queryset=GradeClass.objects.all())
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name','last_name',
                                                 'email','grade_class','photo')




