from django.urls import path
from . import views

app_name = "phones"
urlpatterns = [
    path('registermobile/', views.mobileregistery_form, name='register_mobile'),
    path('registerbrand/', views.brandregistery_form, name='register_brand'),
    path('registermanufacturer/', views.anufacturerregistery_form,name='register_anufacturer'),
    path('updaterecord/', views.update_record, name='update_record'),
    path('reports/', views.report, name='report')
]
