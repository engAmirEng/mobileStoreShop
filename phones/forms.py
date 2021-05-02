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


class BrandNatReportForm(forms.Form):
    choices = [(i.nationality, i.nationality) for i in Brand.objects.all()]
    brand_nationality = forms.ChoiceField(label=" ملیت برند ", choices=choices, required=True)


class BrandMobReportForm(forms.Form):
    choices = [(i.name, i.name) for i in Brand.objects.all()]
    brand_name = forms.ChoiceField(label="نام برند ", choices=choices, required=True)


class NatManForm(forms.Form):
    nat_choices = [(i.nationality, i.nationality) for i in Brand.objects.all()]
    brand_nationality = forms.ChoiceField(label=" ملیت برند ", choices=nat_choices, required=True)
    man_choices = [(i.country_name , i.country_name ) for i in Manufacturer.objects.all()]
    manufacturer = forms.ChoiceField(label=" کشور سازنده ", choices=man_choices, required=True)