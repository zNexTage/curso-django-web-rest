from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('home 123')
    #return HTTPResponse

def contact(request):
    return HttpResponse('contato')

def about(request):
    return HttpResponse('sobre')
