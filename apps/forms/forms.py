from django import forms


class NameForm(forms.Form):
    algo_name = forms.CharField(max_length=65)


class PlatformForm(forms.Form):
    platform_choices = (
        ('MT5', 'MT5'),
        ('ProfitChart', 'ProfitChart'),
        ('Binance', 'Binance'),
    )
    platform = forms.ChoiceField(choices=platform_choices)


class MarketForm(forms.Form):
    market_choices = (
        ('B3 - Ações', 'B3 - Ações'),
        ('B3 - Futuros', 'B3 - Futuros'),
        ('Forex', 'Forex'),
    )
    market = forms.ChoiceField(choices=market_choices)


class StopsForm(forms.Form):
    stops_choices = (
        (' - ', ' - '),
        ('Pontos', 'Pontos'),
        ('Financeiro', 'Financeiro'),
        ('Variação (%)', 'Variação (%)'),
        ('Personalizado', 'Personalizado'),
    )
    stops = forms.ChoiceField(choices=stops_choices)
    custom_stop = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'rows': 8, 'cols': 40,
               'placeholder':
               'Ex.: Sistema de Stop utilizando um '
               'multiplicador do indicador ATR.'}))


class GainForm(forms.Form):
    gain_choices = (
        (' - ', ' - '),
        ('Pontos', 'Pontos'),
        ('Financeiro', 'Financeiro'),
        ('Variação (%)', 'Variação (%)'),
        ('Personalizado', 'Personalizado'),
    )
    gains = forms.ChoiceField(choices=gain_choices)
