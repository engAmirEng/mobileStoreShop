from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import MobileForm, BrandForm, ManufacturerForm
from .models import Brand, Manufacturer, Mobiles


def mobileregistery_form(request):
    mobile_form = MobileForm()
    if request.method == "GET":
        return render(request, "templates/phones/register_mobile.html", {"mobile_form": mobile_form})
    else:
        f_mobile_form = MobileForm(request.POST)
        model_names = [i.model_name.lower() for i in Mobiles.objects.all()]
        if f_mobile_form.is_valid() and request.POST["model_name"].lower() not in model_names:
            f_mobile_form.save()
            return redirect("/phones/registermobile/")
        else:
            massage = "این گوشی قبلا ثبت شده است"
            return render(request, "templates/phones/register_mobile.html", {"mobile_form": mobile_form, "massage": massage})


def brandregistery_form(request, *massage):
    brand_form = BrandForm()
    brand_names = [i.name.lower() for i in Brand.objects.all()]
    if request.method == "GET":
        return render(request, "templates/phones/register_brand.html", {"brand_form": brand_form})
    else:
        f_brand_form = BrandForm(request.POST)
        if f_brand_form.is_valid() and request.POST["name"].lower() not in brand_names:
            f_brand_form.save()
            return redirect("/phones/registermobile/")
        else:
            massage = "این برند قبلا ثبت شده است"
            return render(request, "templates/phones/register_brand.html", {"brand_form": brand_form, "massage": massage})


def anufacturerregistery_form(request):
    manufacturer_form = ManufacturerForm()
    country_names = [i.country_name.lower()
                     for i in Manufacturer.objects.all()]
    if request.method == "GET":
        return render(request, "templates/phones/register_manufacturer.html",
                      {"manufacturer_form": manufacturer_form})
    else:
        f_manufacturer_form = ManufacturerForm(request.POST)
        if f_manufacturer_form.is_valid() and request.POST["country_name"].lower() not in country_names:
            f_manufacturer_form.save()
            return redirect("/phones/registerbrand/")
        else:
            massage = "این سازنده قبلا ثبت شده است"
            return render(request, "templates/phones/register_manufacturer.html",
                          {"manufacturer_form": manufacturer_form,  "massage": massage})
