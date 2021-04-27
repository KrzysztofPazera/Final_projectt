from datetime import date

from django.db import models

from Car_Base.models import CarModel, CarBrand, PartsCategory, CarParts
from Workers.models import Types, Workers


# Create your models here.

# #Model wyceny naprawy samochodu(wersja nie uzywana)

class Repair_costs(models.Model):
    name_owner = models.CharField(max_length=50)
    surname_owner = models.CharField(max_length=50)
    date_of_accident = models.DateField(default=date.today)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, null=True)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True)
    parts_category = models.ManyToManyField(PartsCategory)
    car_parts = models.ManyToManyField(CarParts)
    cost = models.FloatField(default=0.00)


# Model klienta
class Client(models.Model):
    name = models.CharField(max_length=150)
    product = models.ManyToManyField(CarParts, blank=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    product = models.ForeignKey(CarParts, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    quantiti = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product}'

    def get_cart_items(self):
        return self.product
    # def get_quantiti_total(self):
    #     return sum(q for q in self.quantiti)
        # return sum(qs for qs in self.quantiti.all)

    def get_cart_total(self):

        return sum(p for p in self.product.price.all())



class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)

    def get_cart_items(self):
        return self.items.all()

    def __str__(self):
        return '{0} - {1}'.format(self.client, self.ref_code)
