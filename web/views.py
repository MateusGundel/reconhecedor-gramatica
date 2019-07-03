from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, Http404
import json
import daemon.reconhecedor.gramatica as gramatica
import daemon.reconhecedor.consistencia as consistencia
import daemon.reconhecedor.sentencas as sentencas
import daemon.transformar.transformar_glc as transformar_glc


# Create your views here.
def home_view(request):
    return render(request, 'web/home.html')


@csrf_exempt
def reconhecer(request):
    if request.method == 'POST':
        object_from_view = json.loads(request.body)
        response_data = {}
        correto, mensagem = consistencia.verifica(object_from_view)
        if correto:
            tipo_gramatica = gramatica.verifica(object_from_view)
            sentencas_list = sentencas.generate(object_from_view)
            response_data.update({'gramatica':tipo_gramatica})
            response_data.update({'sentencas': sentencas_list})
            response_data.update({'message': "Reconhecimento OK!"})
        else:
            response_data.update({'message': mensagem})

        print(response_data)
        return HttpResponse(
            json.dumps(response_data)
        )
    else:
        raise Http404

@csrf_exempt
def transformar(request):
    if request.method == 'POST':
        object_from_view = json.loads(request.body)
        response_data = {}

        transformar_glc.transformation(object_from_view)

        response_data.update({'message': "Transformacao OK!"})
        print(response_data)
        return HttpResponse(
            json.dumps(response_data)
        )
    else:
        raise Http404
