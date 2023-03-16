from django.shortcuts import render

from .forms import GainForm, MarketForm, NameForm, PlatformForm, StopsForm
from .mt5 import mt5


def home(request):
    return render(request, 'pages/home.html')


def mt5_view(request):
    return mt5(request)


def algotrading(request):
    if request.method == 'POST':
        counter = int(request.POST.get('counter', 0)) + 1

        name_form = NameForm(request.POST)
        if name_form.is_valid():
            algo_name = name_form.cleaned_data['algo_name']
            request.session['algo_name'] = algo_name
    else:
        counter = int(request.GET.get('counter', 0))
        name_form = NameForm()  # Create an empty instance of NameForm

    template_map = {
        0: ('partials/base_algo.html', name_form),
        1: ('partials/platform.html', PlatformForm),
        2: ('partials/market.html', MarketForm),
        3: ('partials/stops.html', StopsForm),
        4: ('partials/gains.html', GainForm)
    }
    partial_template, form_class = template_map.get(
        counter % len(template_map), ('partials/base_algo.html', None))
    form = form_class() if form_class and callable(form_class) else None

    # Get the algo_name from the session
    algo_name = request.session.get('algo_name', '')
    # Delete the algo_name from the session if the page is refreshed
    if 'refresh' in request.GET:
        request.session.pop('algo_name', None)

    context = {
        'partial_template': partial_template,
        'counter': counter,
        'page_name': 'Algotrading',
        'form': form,
        'num_templates': len(template_map)-1,
        'algo_name': algo_name
    }

    return render(request, 'pages/algotrading.html', context)
