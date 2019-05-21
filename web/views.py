from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, Http404
import json
from daemon.functions import Functions


# Create your views here.
def home_view(request):
    return render(request, 'web/home.html')


@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        functions = Functions()
        functions.process(json.loads(request.body))
        response_data = "respondeu"
        return HttpResponse(
            json.dumps(response_data)
        )
    else:
        raise Http404
