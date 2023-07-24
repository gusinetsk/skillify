from django import forms
from .models import Student
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = ('name', 'surname', 'email', 'password', 'password_confirmation')

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