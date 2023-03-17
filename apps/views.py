import json

from django.shortcuts import render

from .forms import GainForm, MarketForm, NameForm, PlatformForm, StopsForm
from .mt5 import mt5


def home(request):
    return render(request, 'pages/home.html')


def mt5_view(request):
    return mt5(request)


def algotrading(request):
    counter = int(request.POST.get('counter', request.GET.get('counter', 0)))

    template_map = {
        0: ('partials/base_algo.html', {'form': NameForm()}),
        1: ('partials/platform.html', {'form': PlatformForm()}),
        2: ('partials/market.html', {'form': MarketForm()}),
        3: ('partials/stops.html', {'form': StopsForm()}),
        4: ('partials/gains.html', {'form': GainForm()})
    }

    if request.method == 'POST':
        direction = request.POST.get('direction', 'next')

        if direction == 'next':
            counter += 1
        else:
            counter -= 1

        # Name saving
        name_form = NameForm(request.POST)
        if name_form.is_valid():
            algo_name = name_form.cleaned_data['algo_name']
            request.session['algo_name'] = algo_name

        # Platform saving
        platform_form = PlatformForm(request.POST)
        if platform_form.is_valid():
            selected_platforms = platform_form.cleaned_data[
                'selected_platforms'].split(',')
            selected_platforms = list(
                filter(lambda x: x.strip() != '', selected_platforms))
            request.session['selected_platforms'] = selected_platforms

        selected_platforms = request.session.get('selected_platforms', [])

        # Market saving
        market_form = MarketForm(request.POST)
        if market_form.is_valid():
            selected_markets = market_form.cleaned_data[
                'selected_markets'].split(',')
            selected_markets = list(
                filter(lambda x: x.strip() != '', selected_markets))
            request.session['selected_markets'] = selected_markets

        selected_markets = request.session.get('selected_markets', [])

        # Stop saving
        stop_form = StopsForm(request.POST)
        if stop_form.is_valid():
            selected_stops = stop_form.cleaned_data[
                'selected_stops'].split(',')
            selected_stops = list(
                filter(lambda x: x.strip() != '', selected_stops))
            request.session['selected_stops'] = selected_stops

        selected_stops = request.session.get('selected_stops', [])

    else:
        name_form = NameForm()

    partial_template, context_dict = template_map.get(
        counter % len(template_map), (
            'partials/base_algo.html', {'form': None}))

    context_dict.update({
        'partial_template': partial_template,
        'counter': counter,
        'num_templates': len(template_map)-1,
        'algo_name': request.session.get('algo_name', ''),
        'platform_name': json.dumps(
            request.session.get('selected_platforms', [])),
        'market_type': json.dumps(
            request.session.get('selected_markets', [])),
        'stop_type': json.dumps(
            request.session.get('selected_stops', []))
    })

    return render(request, 'pages/algotrading.html', context_dict)
