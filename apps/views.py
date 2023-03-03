from django.http import HttpResponse  # noqa: F401
from django.shortcuts import render

from apps.utils.altoinvest.factory import make_robot

# from .models import Set_stoploss
from .mt5 import mt5


# Direciona para o APP de validação de licença do EA no MT5
def mt5_view(request):
    return mt5(request)


def home(request):
    return render(request, 'pages/home.html', context={
        'robot': make_robot(),
    })


