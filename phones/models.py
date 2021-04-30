from django.db import models


class Manufacturer(models.Model):
    country_name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.country_name


class Brand(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Mobiles(models.Model):
    model_name = models.CharField(max_length=50, primary_key=True)
    color = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    screen_size = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField()
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.DO_NOTHING)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name
