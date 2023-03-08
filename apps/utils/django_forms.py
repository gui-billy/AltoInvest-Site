import re

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
