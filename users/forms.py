import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Senha deve conter pelo menos 8 caracteres '
            'número, letra maiúscula e minúscula'
        ),
            code='invalid'
        )


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Primeiro nome:',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ex.: João'}),
    )
    last_name = forms.CharField(
        label='Último nome:',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ex.: Silva'}),
    )
    username = forms.CharField(
        label='Usuário:',
        required=True,
        help_text='Mínimo de 4 caracteres',
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuário'}),
    )
    email = forms.CharField(
        label='Endereço de email:',
        required=True,
        help_text='Digite um e-mail válido',
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'}),
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha'
        }),
        help_text=(
            'Senha deve conter pelo menos 6 caracteres '
            'número, letra maiúscula e minúscula'
        )

    )
    password2 = forms.CharField(
        label='Confirmar Senha',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repita sua senha'
        })
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'As senhas digitadas devem ser iguais',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })
