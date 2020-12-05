from django import forms
from django.core.exceptions import ValidationError

from account.models import User


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Usuário', min_length=4, max_length=150)
    first_name = forms.CharField(label='Nome', min_length=4, max_length=150)
    last_name = forms.CharField(label='Sobrenome', min_length=4, max_length=150)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Digite uma senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Usuário já cadastrado.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("E-mail já cadastrado.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas digitadas são diferentes.")

        return password2

    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['first_name'],
            self.cleaned_data['last_name'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
