from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Christian'
    })
    #return HTTPResponse


def recipes(request, id):
    return render(request, 'recipes/pages/recipe_view.html', context={
        'name': 'Christian'
    })


# def contact(request):
#     return render(request, 'recipes/contact.html')

# def about(request):
#     return HttpResponse('sobre')
