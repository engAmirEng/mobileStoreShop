from django import forms
from .models import Mobiles, Manufacturer, Brand


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = [i.name for i in Mobiles._meta.get_fields()]
        labels = {"model_name": "مدل گوشی", "color": "رنگ",
                  "price": "قیمت", "screen_size": "سایز صفحه نمایش",
                  "in_stock": "وضعیت", "manufacturer": "کشور سازنده", "brand": "نام برند"}


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "nationality"]
        labels = {"name": "نام برند", "nationality": "ملیت برند"}


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ["country_name"]
        labels = {"country_name": "کشور سازنده"}
