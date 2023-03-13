from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'pages/register_view.html', {
        'form': form,
        'form_action': reverse('users:create'),
        'page_name': 'Register'
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    form = RegisterForm(request.POST)

    if form.is_valid():
        form.save()
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        if 'register_form_data' in request.session:
            del request.session['register_form_data']
            return redirect(reverse('users:login'))
        return redirect('users:login')
    else:
        request.session['register_form_data'] = request.POST
        return redirect('users:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'pages/login.html', {
        'form': form,
        'form_action': reverse('users:login_create'),
        'page_name': 'Login'
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Login efetuado')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Usuário ou senha inválida')
    else:
        messages.error(request, 'Usuário ou senha inválida')

    return redirect(reverse('users:dashboard'))


@login_required(login_url='users:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('users:login'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('users:login'))

    logout(request)
    return redirect(reverse('users:login'))


@login_required(login_url='users:login', redirect_field_name='next')
def dashboard(request):
    return render(request, 'pages/dashboard.html', {
        'page_name': 'Dashboard'
    })
