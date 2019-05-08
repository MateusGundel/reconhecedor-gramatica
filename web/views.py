from django.shortcuts import render


# Create your views here.
def home_view(request):
    data = {}
    data.update({'var': 'O app funcionou'})
    return render(request, 'web/home.html', data)
