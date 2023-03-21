import json

from django.shortcuts import render

from .forms import (GainForm, HoursForm, MarketForm, NameForm, OrderForm,
                    PlatformForm, StopsForm)
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
        4: ('partials/gains.html', {'form': GainForm()}),
        5: ('partials/order.html', {'form': OrderForm()}),
        6: ('partials/hours.html', {'form': HoursForm()}),
        7: ('partials/apply.html', {}),
    }

    if request.method == 'POST':
        direction = request.POST.get('direction', 'next')

        if direction == 'next':
            counter += 1
        else:
            counter -= 1

        # Generic view function
        def view_request(_Form, selected_key):
            _form = _Form(request.POST)
            if _form.is_valid():
                selected = _form.cleaned_data[selected_key].split(',')
                selected = list(filter(lambda x: x.strip() != '', selected))
                request.session[selected_key] = selected

            return request.session.get(selected_key, [])

        # Name saving
        name_form = NameForm(request.POST)
        if name_form.is_valid():
            algo_name = name_form.cleaned_data['algo_name']
            request.session['algo_name'] = algo_name
        # Platform saving
        selected_platforms = view_request(PlatformForm, 'selected_platforms')  # noqa: F841, E501
        # Market saving
        selected_markets = view_request(MarketForm, 'selected_markets')  # noqa: F841, E501
        # Stop saving
        selected_stops = view_request(StopsForm, 'selected_stops')  # noqa: F841, E501
        # Gain saving
        selected_gains = view_request(GainForm, 'selected_gains')  # noqa: F841, E501
        # Order saving
        selected_orders = view_request(OrderForm, 'selected_orders')  # noqa: F841, E501
        # Hour saving
        selected_hours = view_request(HoursForm, 'selected_hours')  # noqa: F841, E501

    else:
        name_form = NameForm()

    partial_template, context_dict = template_map.get(
        counter % len(template_map), (
            'partials/base_algo.html', {'form': None}))

    def jdumps(key):
        return json.dumps(request.session.get(key, []), ensure_ascii=False)

    keys = [
        {'name': 'algo_name', 'label': 'Nome'},
        {'name': 'selected_platforms', 'label': 'Plataforma'},
        {'name': 'selected_markets', 'label': 'Tipo de Mercado'},
        {'name': 'selected_stops', 'label': 'Sistema de Stop-Loss'},
        {'name': 'selected_gains', 'label': 'Sistema de Stop-Gain'},
        {'name': 'selected_orders', 'label': 'Tipo de Ordem'},
        {'name': 'selected_hours', 'label': 'Horário de Negociação'},
    ]

    session_data = [
        (key['name'].replace('selected_', ''),
         jdumps(key['name'])) for key in keys
    ]

    session_data_json = json.dumps(session_data)

    context_dict.update({
        'partial_template': partial_template,
        'counter': counter,
        'num_templates': len(template_map) - 1,
        'algo_name': request.session.get('algo_name', ''),
        'platform_name': jdumps('selected_platforms'),
        'market_type': jdumps('selected_markets'),
        'stop_type': jdumps('selected_stops'),
        'gain_type': jdumps('selected_gains'),
        'order_type': jdumps('selected_orders'),
        'hour_type': jdumps('selected_hours'),
        'session_data_json': session_data_json,
        'keys_json': json.dumps(keys),
    })

    return render(request, 'pages/algotrading.html', context_dict)
