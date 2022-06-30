from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', context={
        'name': 'Christian'
    })
    #return HTTPResponse

def contact(request):
    return render(request, 'temp.html')

def about(request):
    return HttpResponse('sobre')
