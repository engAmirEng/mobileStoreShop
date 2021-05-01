from django.contrib import admin
from django.urls import path, include
from phones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("phones/", include("phones.urls")),
    path("", views.index)
]
