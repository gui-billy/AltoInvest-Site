from django.test import TestCase
from parameterized import parameterized

from users.forms import RegisterForm


class UsersRegisterFormTest(TestCase):
    @parameterized.expand([
        ('username', 'Digite seu usuário'),
        ('email', 'Digite seu e-mail'),
        ('first_name', 'Ex.: João'),
        ('last_name', 'Ex.: Silva'),
        ('password', 'Digite sua senha'),
        ('password2', 'Repita sua senha'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand([
        ('username', (
            'Mínimo de 4 caracteres')),
        ('email', 'Digite um e-mail válido'),
        ('password', (
            'Senha deve conter pelo menos 6 caracteres '
            'número, letra maiúscula e minúscula'
        )),
    ])
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)

    @parameterized.expand([
        ('username', 'Usuário:'),
        ('first_name', 'Primeiro nome:'),
        ('last_name', 'Último nome:'),
        ('email', 'Endereço de email:'),
        ('password', 'Senha'),
        ('password2', 'Confirmar Senha'),
    ])
    def test_fields_label(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)
