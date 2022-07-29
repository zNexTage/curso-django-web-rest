from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    #Path -> Rota, View
    path('', views.home, name='home'), # Home
    path('<int:id>/', views.recipes, name='recipe')
    # path('sobre/', about), # /sobre/
    # path('contato/', contact), # /contato/
]
