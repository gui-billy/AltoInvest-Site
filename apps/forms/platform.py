from django import forms


class PlatformForm(forms.Form):
    platform_choices = (
        ('MT5', 'MT5'),
        ('ProfitChart', 'ProfitChart'),
        ('Binance', 'Binance'),
    )
    platform = forms.ChoiceField(choices=platform_choices)
