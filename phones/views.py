from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.utils import timezone
from .forms import MobileForm, BrandForm, ManufacturerForm
from .models import Brand, Manufacturer, Mobiles


def index(request):
    return render(request, "templates/index.html")


# mobile registery form
def mobileregistery_form(request):
    mobile_form = MobileForm()
    if request.method == "GET":
        return render(request, "templates/phones/register_mobile.html", {"mobile_form": mobile_form})
    else:
        f_mobile_form = MobileForm(request.POST)
        model_names = [i.model_name.lower() for i in Mobiles.objects.all()]
        # check the existance of the model_name with no case sensitivity
        if f_mobile_form.is_valid() and request.POST["model_name"].lower() not in model_names:
            f_mobile_form.save()
            return redirect(f"/phones/registermobile/")
        else:
            massage = "این گوشی قبلا ثبت شده است"
            return render(request, "templates/phones/register_mobile.html", {"mobile_form": mobile_form, "massage": massage})


# barnd registery form
def brandregistery_form(request):
    brand_form = BrandForm()
    brand_names = [i.name.lower() for i in Brand.objects.all()]
    if request.method == "GET":
        return render(request, "templates/phones/register_brand.html", {"brand_form": brand_form})
    else:
        f_brand_form = BrandForm(request.POST)
        # check the validity case insensitivitivly
        if f_brand_form.is_valid() and request.POST["name"].lower() not in brand_names:
            f_brand_form.save()
            return redirect("/phones/registermobile/")
        else:
            massage = "این برند قبلا ثبت شده است"
            return render(request, "templates/phones/register_brand.html", {"brand_form": brand_form, "massage": massage})


# manufacturer registery form
def anufacturerregistery_form(request):
    manufacturer_form = ManufacturerForm()
    country_names = [i.country_name.lower()
                     for i in Manufacturer.objects.all()]
    if request.method == "GET":
        return render(request, "templates/phones/register_manufacturer.html",
                      {"manufacturer_form": manufacturer_form})
    else:
        f_manufacturer_form = ManufacturerForm(request.POST)
        # check the validity case insensitivitivly
        if f_manufacturer_form.is_valid() and request.POST["country_name"].lower() not in country_names:
            f_manufacturer_form.save()
            return redirect("/phones/registerbrand/")
        else:
            massage = "این سازنده قبلا ثبت شده است"
            return render(request, "templates/phones/register_manufacturer.html",
                          {"manufacturer_form": manufacturer_form,  "massage": massage})


# updating form
def update_record(request):
    if request.method == "GET":
        status = "search"
        return render(request, "templates/phones/update_record.html", {"status": status})
    # if the request is in getting mobile info for update stage
    elif "model_name_update" in request.POST:
        status = "update"
        filled_form = ""
        massage = ""
        # try if the model_name entered for updating even exist
        try:
            get_object_or_404(Mobiles, pk=request.POST["model_name_update"])
            updating_obj = Mobiles.objects.filter(
                model_name=request.POST["model_name_update"])
            # provide the initial value for updating form
            initial = {"model_name": updating_obj[0].model_name, "color": updating_obj[0].color,
                       "price": updating_obj[0].price, "screen_size": updating_obj[0].screen_size,
                       "in_stock": updating_obj[0].in_stock, "manufacturer": updating_obj[0].manufacturer,
                       "brand": updating_obj[0].brand}
            filled_form = MobileForm(initial=initial)
        except:
            massage = "این گوشی ثبت نشده است"
        return render(request, "templates/phones/update_record.html",
                      {"status": status, "filled_form": filled_form, "massage": massage})
    # check if the request is in submition for perform update stage
    else:
        status = ""
        try:
            updating_obj = get_object_or_404(
                Mobiles, pk=request.POST["model_name"])
            updated_form = MobileForm(request.POST, instance=updating_obj)
            if updated_form.is_valid():
                updated_form.save()
                return redirect("/")
            else:
                massage = "موارد وارد شده معتبر نمی باشد"
        # if the user attempeted to change the model_name
        except:
            massage = "مدل گوشی قابل تغییر نمی باشد"
        return render(request, "templates/phones/update_record.html",
                      {"status": status, "massage": massage})


# for return the Json response
from django.http import JsonResponse
from django.core import serializers
# implemented updating forms
from .forms import BrandNatReportForm, BrandMobReportForm, NatManForm
# get report form
def report(request):
    if request.method == "GET":
        brand_nat_form = BrandNatReportForm()
        brand_mob_form = BrandMobReportForm()
        nat_man_form = NatManForm()
        form = {"brand_nat_form": brand_nat_form,
                "brand_mob_form": brand_mob_form, "nat_man_form": nat_man_form}
        return render(request, "templates/phones/reports.html", form)
    else:
        # filter based on brand nationality
        if 'brand_nationality' in request.POST and 'manufacturer' not in request.POST:
            brand_nationality = request.POST['brand_nationality']
            obj = Brand.objects.filter(nationality=brand_nationality)
            obj_json = serializers.serialize("json", obj)
            data = {"Brands": obj_json}
            return JsonResponse(data)
        # filter based on brand name
        elif 'brand_name' in request.POST:
            brand_names = request.POST["brand_name"]
            obj = Mobiles.objects.filter(brand=brand_names)
            obj_json = serializers.serialize("json", obj)
            data = {"Mobiles": obj_json}
            return JsonResponse(data)
        # filter based on brand nationality and manufacturer natioanily
        elif 'brand_nationality' and 'manufacturer' in request.POST:
            brand_nationality = request.POST["brand_nationality"]
            manufacturer = request.POST["manufacturer"]
            obj = Mobiles.objects.filter(
                brand__nationality=brand_nationality, manufacturer=manufacturer)
            obj_json = serializers.serialize("json", obj)
            data = {"Mobiles": obj_json}
            return JsonResponse(data)
        # filter based on equivalency of brand nationality and manufacturer natioanily
        elif "get_native" in request.POST:
            sql_query = "SELECT model_name, color, in_stock, brand_id, manufacturer_id, screen_size, \
                nationality as brand_nationality FROM (SELECT * FROM phones_mobiles LEFT JOIN phones_brand on \
                    phones_mobiles.brand_id = phones_brand.name) WHERE nationality = manufacturer_id"
            obj = Mobiles.objects.raw(sql_query)
            obj_json = serializers.serialize("json", obj)
            data = {"Mobiles": obj_json}
            return JsonResponse(data)
