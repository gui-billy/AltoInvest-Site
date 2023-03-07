from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'pages/register_view.html', {
        'form': form,
        'page_name': 'Register'
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    form = RegisterForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        del request.session['register_form_data']
        return redirect('users:register')
    else:
        request.session['register_form_data'] = request.POST
        return redirect('users:register')
