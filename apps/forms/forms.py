from django import forms


class NameForm(forms.Form):
    algo_name = forms.CharField()


class PlatformForm(forms.Form):
    platform_choices = (
        ('MT5', 'MT5'),
        ('ProfitChart', 'ProfitChart'),
        ('Binance', 'Binance'),
    )
    platform = forms.ChoiceField(choices=platform_choices)
    selected_platforms = forms.CharField(
        widget=forms.HiddenInput(), required=False)


class MarketForm(forms.Form):
    market_choices = (
        ('B3 - Ações', 'B3 - Ações'),
        ('B3 - Futuros', 'B3 - Futuros'),
        ('Forex', 'Forex'),
    )
    market = forms.ChoiceField(choices=market_choices)
    selected_markets = forms.CharField(
        widget=forms.HiddenInput(), required=False)


class StopsForm(forms.Form):
    stops_choices = (
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
    selected_stops = forms.CharField(
        widget=forms.HiddenInput(), required=False)


class GainForm(forms.Form):
    gain_choices = (
        ('Pontos', 'Pontos'),
        ('Financeiro', 'Financeiro'),
        ('Variação (%)', 'Variação (%)'),
        ('Personalizado', 'Personalizado'),
    )
    gains = forms.ChoiceField(choices=gain_choices)
    custom_gain = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'rows': 8, 'cols': 40,
               'placeholder':
               'Ex.: Sistema de Gain utilizando um '
               'multiplicador do indicador ATR.'}))
    selected_gains = forms.CharField(
        widget=forms.HiddenInput(), required=False)


class OrderForm(forms.Form):
    order_choices = (
        ('A Mercado', 'A Mercado'),
        ('Limit', 'Limit'),
        ('Stop', 'Stop'),
    )
    orders = forms.ChoiceField(choices=order_choices)
    custom_order = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'rows': 8, 'cols': 40,
               'placeholder':
               'Ex.: Envio de ordem baseado na '
               'distancia em pontos.'}))
    selected_orders = forms.CharField(
        widget=forms.HiddenInput(), required=False)


class HoursForm(forms.Form):
    hour_choices = (
        ('Horário Fixo', 'Horário Fixo'),
        ('Horário Início', 'Horário Início'),
        ('Horário Fim', 'Horário Fim'),
        ('Horário Encerramento', 'Horário Encerramento'),
        ('Personalizado', 'Personalizado'),
    )
    hours = forms.ChoiceField(choices=hour_choices)
    custom_hour = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'rows': 8, 'cols': 40,
               'placeholder':
               'Ex.: Todos os dias colocar uma '
               'ordem às 11:00h.'}))
    selected_hours = forms.CharField(
        widget=forms.HiddenInput(), required=False)
    extra_input = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'extra-input', 'placeholder': 'Insira o valor'}))
