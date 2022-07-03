from django.urls import path

from recipes.views import home

urlpatterns = [
    #Path -> Rota, View
    path('', home), # Home
    # path('sobre/', about), # /sobre/
    # path('contato/', contact), # /contato/
]
