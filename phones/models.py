from django.db import models


class Manufacturer(models.Model):
    country_name = models.CharField(max_length=50, primary_key=True)


class Brand(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    nationality = models.CharField(max_length=50)


class Mobiles(models.Model):
    model_name = models.CharField(max_length=50, primary_key=True)
    color = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    screenSize = models.PositiveIntegerField()
    inStock = models.BooleanField()
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.DO_NOTHING)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
