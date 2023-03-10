from django.http import HttpResponse  # noqa: F401
from django.shortcuts import render

from apps.utils.altoinvest.factory import make_robot

from .forms import PlatformForm
from .mt5 import mt5


def home(request):
    return render(request, 'pages/home.html', context={
        'robot': make_robot(),
    })


def mt5_view(request):
    return mt5(request)


def algotrading(request):
    form = PlatformForm()
    return render(request, 'pages/algotrading.html', context={
        'page_name': 'Algotrading',
        'form': form,
    })
