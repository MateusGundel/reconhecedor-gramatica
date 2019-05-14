from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, Http404
import json


# Create your views here.
def home_view(request):
    return render(request, 'web/home.html')


@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        print(request.POST)
        response_data = dict(request.POST)
        print(response_data)
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        raise Http404
