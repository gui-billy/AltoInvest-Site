from django.contrib import admin

from .models import Clients


@admin.register(Clients)
class CClient(admin.ModelAdmin):
    list_display = ['id', 'name', 'broker', 'account', 'exp_date']
    list_display_links = 'name',
    search_fields = 'id', 'name', 'broker', 'account', 'exp_date',
    list_filter = 'name', 'broker', 'account', 'exp_date',
    list_per_page = 10
    list_editable = 'exp_date',
    ordering = 'name',
