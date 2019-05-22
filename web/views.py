from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, Http404
import json
import daemon.gramatica as gramatica
import daemon.consistencia as consistencia
import daemon.sentencas as sentencas


# Create your views here.
def home_view(request):
    return render(request, 'web/home.html')


@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        object_from_view = json.loads(request.body)
        response_data = {}
        correto, mensagem = consistencia.verifica(object_from_view)
        if correto:
            tipo_gramatica = gramatica.verifica(object_from_view)
            sentencas_list = sentencas.generate(object_from_view)
            response_data.update({'gramatica':tipo_gramatica})
            response_data.update({'sentencas': sentencas_list})
            response_data.update({'message': "Processamento OK"})
        else:
            response_data.update({'message': mensagem})

        print(response_data)
        return HttpResponse(
            json.dumps(response_data)
        )
    else:
        raise Http404
