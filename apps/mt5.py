from datetime import datetime

from django.http import JsonResponse

from .models import Clients


def mt5(request):
    if request.method == 'GET':
        data = request.GET.dict()
        if not data:
            response_data = {"ERRO": 'Dados inválidos'}
            return JsonResponse(response_data, status=400, json_dumps_params={'ensure_ascii': False})  # noqa: E501
        data_tuple = tuple(data.items())

        clients = Clients.objects.all().values('broker', 'account', 'exp_date')
        for client in clients:
            if (data_tuple[0][1] == client["broker"]) and (int(data_tuple[1][1]) == client["account"]):  # noqa: E501
                dtt = datetime.strptime(
                    str(client["exp_date"]), "%Y-%m-%d").date()
                if (datetime.now().date() < dtt):
                    exp_date = dtt.strftime("%d-%m-%Y")
                    response_data = {
                        "broker": client["broker"], "account": client["account"], "exp_date": exp_date}  # noqa: E501
                    return JsonResponse(response_data, status=200, json_dumps_params={'ensure_ascii': False})  # noqa: E501
                else:
                    exp_date = datetime.strptime(
                        str(client["exp_date"]), "%Y-%m-%d").strftime("%d-%m-%Y")  # noqa: E501
                    response_data = {
                        "ERRO": 'Licença Expirada', "Data": exp_date}
                    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})  # noqa: E501
        response_data = {"ERRO": 'Conta Inválida'}
        return JsonResponse(response_data, status=400, json_dumps_params={'ensure_ascii': False})  # noqa: E501

    response_data = {"ERRO": 'Método Inválido'}
    return JsonResponse(response_data, status=405, json_dumps_params={'ensure_ascii': False})  # noqa: E501
