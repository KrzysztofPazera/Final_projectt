from django.db import models
from datetime import date
# Create your models here.

from Workers.models_workers import Types, Workers
from Car_Base.models import CarModel, CarBrand, PartsCategory, CarParts

# #Model wyceny naprawy samochodu
# Pierwszy krok wybór samochodu
class Repair_costs(models.Model):
    name_owner= models.CharField(max_length=50)
    surname_owner = models.CharField(max_length=50)
    date_of_accident = models.DateField(default=date.today())
    car_brand= models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    car_model= models.ForeignKey(CarModel, on_delete=models.CASCADE)
    parts_category= models.ManyToManyField(PartsCategory)
    car_parts= models.ManyToManyField(CarParts)
    cost = models.FloatField(default=0.00)

