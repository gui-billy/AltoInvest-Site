from django.http import HttpResponse  # noqa: F401
from django.shortcuts import render

from siteapps.models import Stoploss
from siteapps.utils.projetos.factory import make_robot

# from .models import Set_stoploss
from .mt5 import mt5


# Direciona para o APP de validação de licença do EA no MT5
def mt5_view(request):
    return mt5(request)


def home(request):
    return render(request, 'pages/home.html', context={
        'robot': make_robot(),
    })


def login(request, id):
    return render(request, 'pages/home.html')


def dropdown_view(request):
    stoploss_list = Stoploss.objects.all()
    context = {'stoploss_list': stoploss_list}
    return render(request, 'pages/algotrading.html', context)
