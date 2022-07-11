from django.urls import path

from . import views

urlpatterns = [
    #Path -> Rota, View
    path('', views.home), # Home
    path('<int:id>/', views.recipes)
    # path('sobre/', about), # /sobre/
    # path('contato/', contact), # /contato/
]
