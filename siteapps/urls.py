from django.urls import path

from . import views
from .views import dropdown_view

# from .views import suspend_list

urlpatterns = [
    path('', views.home, name='home'),  # Home
    path('mt5/', views.mt5_view, name='MT5 license'),  # Check MT5 License
    path('login/<int:id>/', views.login, name='login'),
    path('algotrading/', dropdown_view, name='algotrading'),
]
