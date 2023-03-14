# from django.http import HttpResponse
from django.shortcuts import render

from .forms import GainForm, MarketForm, PlatformForm, StopsForm
from .mt5 import mt5


def home(request):
    return render(request, 'pages/home.html')


def mt5_view(request):
    return mt5(request)


def algotrading(request):
    # default value of 0 if not present in GET params
    counter = request.GET.get('counter', 0)
    counter = int(counter)  # ensure counter is an integer
    template_map = {
        0: ('partials/base_algo.html', None),
        1: ('partials/platform.html', PlatformForm),
        2: ('partials/market.html', MarketForm),
        3: ('partials/stops.html', StopsForm),
        4: ('partials/gains.html', GainForm)
    }
    partial_template, form_class = template_map.get(
        counter % len(template_map), ('partials/base_algo.html', None))
    form = form_class() if form_class else None

    context = {
        'partial_template': partial_template,
        'counter': counter,
        'page_name': 'Algotrading',
        'form': form,
        'num_templates': len(template_map)-1
    }

    return render(request, 'pages/algotrading.html', context)
