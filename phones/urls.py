from django.urls import path

from . import views

urlpatterns = [
    path('registermobile', views.registery_forms, name='index'),
]
