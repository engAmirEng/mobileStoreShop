from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import MobileForm, BrandForm, ManufacturerForm
from .models import Brand, Manufacturer, Mobiles


def index(request):
    return render(request, "templates/index.html")


def mobileregistery_form(request):
    mobile_form = MobileForm()
    if request.method == "GET":
        return render(request, "templates/phones/register_mobile.html", {"mobile_form": mobile_form})
    else:
        f_mobile_form = MobileForm(request.POST)
        model_names = [i.model_name.lower() for i in Mobiles.objects.all()]
        if f_mobile_form.is_valid() and request.POST["model_name"].lower() not in model_names:
            f_mobile_form.save()
            return redirect(f"/phones/registermobile/")
        else:
            massage = "این گوشی قبلا ثبت شده است"
            return render(request, "templates/phones/register_mobile.html", {"mobile_form": mobile_form, "massage": massage})


def brandregistery_form(request):
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


def update_record(request):
    if request.method == "GET":
        status = "search"
        return render(request, "templates/phones/update_record.html", {"status": status})
    elif "model_name_update" in request.POST:
        status = "update"
        filled_form = ""
        massage = ""
        try:
            get_object_or_404(Mobiles, pk=request.POST["model_name_update"])
            updating_obj = Mobiles.objects.filter(model_name=request.POST["model_name_update"])
            initial = {"model_name": updating_obj[0].model_name, "color": updating_obj[0].color, 
                    "price": updating_obj[0].price, "screen_size": updating_obj[0].screen_size, 
                    "in_stock": updating_obj[0].in_stock, "manufacturer": updating_obj[0].manufacturer, 
                    "brand": updating_obj[0].brand}
            filled_form = MobileForm(initial=initial)
        except:
            massage = "این گوشی ثبت نشده است"
        return render(request, "templates/phones/update_record.html", \
                                            {"status": status, "filled_form": filled_form, "massage":massage})
    else:
        status = ""
        try:
            updating_obj = get_object_or_404(Mobiles, pk=request.POST["model_name"])
            updated_form = MobileForm(request.POST, instance=updating_obj)
            if updated_form.is_valid():
                updated_form.save()
                return redirect("/")
            else:
                massage = "موارد وارد شده معتبر نمی باشد"
        # updating_obj = Mobiles.objects.get(pk=request.POST["model_name"])
        except:
            massage = "مدل گوشی قابل تغییر نمی باشد"
        return render(request, "templates/phones/update_record.html", \
                                        {"status": status, "massage":massage})

    
