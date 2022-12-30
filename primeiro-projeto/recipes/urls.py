from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    # Path -> Rota, View
    path('', views.home, name='home'),  # Home
    path('recipes/category/<int:category_id>/',
         views.category, name='category'),
    path('recipes/<int:id>/', views.recipes, name='recipe')
    # path('sobre/', about), # /sobre/
    # path('contato/', contact), # /contato/
]
