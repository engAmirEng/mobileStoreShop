from django.contrib import admin
from django.urls import path, include
from phones import views, models

movie_resource = models.MobileResource()
urlpatterns = [
    path('admin/', admin.site.urls),
    path("phones/", include("phones.urls")),
    path("", views.index),
    path("api/", include(movie_resource.urls))
]
