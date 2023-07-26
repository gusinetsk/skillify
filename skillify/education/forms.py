from django import forms
from .models import Student
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = ('name', 'surname','sex','email','course')

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if len(password) < 8:
    #         raise ValidationError("Пароль должен быть не менее 8 символов")
    #     return password
    def clean_password2(self):
        password = self.cleaned_data.get('password1')
        confirm_password = self.cleaned_data.get('password2')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')

        return confirm_password

    def save(self, commit=True):
        student = super().save(commit=False)
        password = self.cleaned_data['password1']
        student.set_password(password)
        if commit:
            student.save()
        return student