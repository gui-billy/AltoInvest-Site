from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário:',
        required=True,
        error_messages={
            'required': 'Escreva seu usuário',
        },
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu usuário'}),
    )
    password = forms.CharField(
        label='Senha:',
        required=True,
        error_messages={'required': 'Campo senha não pode ser vazio'},
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha'
        }),


    )
