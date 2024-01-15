from django.urls import path
from .views import adauga_carte

urlpatterns = [
    path('add/', adauga_carte, name='adauga_carte'),
]