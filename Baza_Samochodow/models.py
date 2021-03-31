from django.db import models

# Klasa marki samochodu
from django.urls import reverse


class CarBrand(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_detail_url(self):
        return f'car_models/{self.id}'

#Klasa modelu samochodu
class CarModel(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    engine= models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_detail_url(self):
        return f'{self.id}/'

# Klasy częśći samochodowych
# Klasa kategorii
class PartsCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def get_detail_url(self):
        return f'parts_list/{self.id}'

# Klasa glowna czesci samochodowych
class CarParts(models.Model):
    name = models.CharField(max_length=100)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    id_number_of_product = models.CharField(max_length=150, unique=True)
    category= models.ForeignKey(PartsCategory, on_delete=models.CASCADE)
    price = models.FloatField(default=0.00)
    # def __str__(self):
    #     return f'{self.name},{self.price}'

    def show_name(self):
        return self.name
    def get_detail_url(self):
        return f'{self.id}/'
