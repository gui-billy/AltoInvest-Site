from unittest import TestCase

from django.test import TestCase as DjangoTestCase
from django.urls import reverse
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
        ('email', 'Digite um e-mail válido'),
        ('password', (
            'Senha deve conter pelo menos 8 caracteres '
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


class UserRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@anyemail.com',
            'password': '1',
            'password2': '1',
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand([
        ('username', 'Escreva seu usuário'),
        ('first_name', 'Escreva seu primeiro nome'),
        ('last_name', 'Escreva seu último nome'),
        ('password', 'Campo senha não pode ser vazio'),
        ('password2', 'Repita a senha exatamente como no campo anterior'),
        ('email', 'Digite seu E-mail'),
    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('users:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(field))

    def test_username_field_min_length_should_be_4(self):
        self.form_data['username'] = 'joa'
        url = reverse('users:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'Usuário deve ter pelo menos 4 caracteres'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))

    def test_username_field_max_length_should_be_150(self):
        self.form_data['username'] = 'A' * 31
        url = reverse('users:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'Usuário com máximo de 30 caracteres'

        self.assertIn(msg, response.context['form'].errors.get('username'))
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_password_field_have_lower_upper_case_letters_and_numbers(self):
        self.form_data['password'] = 'abc123'
        url = reverse('users:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = (
            'Senha deve conter pelo menos 8 caracteres '
            'número, letra maiúscula e minúscula'
        )

        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))

        self.form_data['password'] = '@A123abc123'
        url = reverse('users:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertNotIn(msg, response.context['form'].errors.get('password'))

    def test_password_and_password_confirmation_are_equal(self):
        self.form_data['password'] = '@A123abc123'
        self.form_data['password2'] = '@A123abc1235'

        url = reverse('users:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'As senhas digitadas devem ser iguais'

        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))

        self.form_data['password'] = '@A123abc123'
        self.form_data['password2'] = '@A123abc123'

        url = reverse('users:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertNotIn(msg, response.content.decode('utf-8'))

    def test_send_get_request_to_registration_create_view_returns_404(self):
        url = reverse('users:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_email_field_must_be_unique(self):
        url = reverse('users:create')

        self.client.post(url, data=self.form_data, follow=True)
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = 'E-mail já cadastrado'
        self.assertIn(msg, response.context['form'].errors.get('email'))
        self.assertIn(msg, response.content.decode('utf-8'))
