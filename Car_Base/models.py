import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Klasa marki samochodu

class CarBrand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return f'car_models/{self.id}'

    def sum_of_cars(self):
        return CarModel.objects.filter(brand=self).count()


# Klasa modelu samochodu

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


def year_choice():
    return [(r, r) for r in range(1900, datetime.date.today().year + 1)]


class CarModel(models.Model):
    name = models.CharField(max_length=50)
    generacion = models.PositiveIntegerField(default=1)
    year = models.IntegerField(default=current_year, choices=year_choice(),
                               validators=[MinValueValidator(1900), max_value_current_year])
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    engine = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.generacion}, {self.year}, {self.engine}'

    def get_detail_url(self):
        return f'{self.id}/edit_car/'

    def sum_of_cars(self):
        return None


# Klasy częśći samochodowych
# Klasa kategorii
class PartsCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return f'parts_list/{self.id}'
    def sum_of_parts(self):
        return CarParts.objects.filter(category=self).count()


# Klasa glowna czesci samochodowych
class CarParts(models.Model):
    name = models.CharField(max_length=100)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    id_number_of_product = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(PartsCategory, on_delete=models.CASCADE)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return f'{self.name},{self.price}'

    # def __str__(self):
    #     return self.name
    def show_name(self):
        return self.name

    def get_detail_url(self):
        return f'{self.id}/edit_part/'
