from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.data.factory import make_recipe

from recipes.models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(category__pk=category_id).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })
    # return HTTPResponse


def recipes(request, id):
    return render(request, 'recipes/pages/recipe_view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True
    })


# def contact(request):
#     return render(request, 'recipes/contact.html')

# def about(request):
#     return HttpResponse('sobre')
