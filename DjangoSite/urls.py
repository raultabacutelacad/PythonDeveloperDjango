"""
URL configuration for DjangoSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from biblioteca import views as biblioteca_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", biblioteca_views.homepage, name="homepage"),
    path('delete/<int:book_id>',biblioteca_views.confirm_delete_book, name='confirm_delete_book'),
    path('delete/confirm/<int:book_id>', biblioteca_views.delete_book, name='delete_book'),
    path('add', biblioteca_views.adauga_carte, name='adauga_carte'),
    path('rate/<int:id_carte>', biblioteca_views.rating_carte, name='rating_carte'),
    path('read/<int:id_carte>', biblioteca_views.confirm_marcheaza_ca_citit, name='confirm_marcheaza_citit'),
    path('mark-as-read/<int:id_carte>', biblioteca_views.marcheaza_ca_citit, name='confirm_mark_as_read')
]