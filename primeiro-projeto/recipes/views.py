from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.data.factory import make_recipe


# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)]
    })
    #return HTTPResponse


def recipes(request, id):
    return render(request, 'recipes/pages/recipe_view.html', context={
        'recipe': make_recipe()
    })


# def contact(request):
#     return render(request, 'recipes/contact.html')

# def about(request):
#     return HttpResponse('sobre')
