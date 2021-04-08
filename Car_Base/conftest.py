import pytest
from django.test import Client
from django.contrib.auth.models import User, Permission

from Car_Base.models import CarBrand, CarModel


@pytest.fixture
def client():
    c = Client()
    return c


@pytest.fixture
def users():
    users = []
    for x in range(1, 11):
        u = User.objects.create(username=str(x))
        users.append(u)
    return users

@pytest.fixture
def car_brand():
    car_brand = []
    for x in range(1, 11):
        u = CarBrand.objects.create(name=str(x))
        car_brand.append(u)
    return car_brand

@pytest.fixture
def car_model(car_brand):
    count = 1
    year = 1990
    car_model = []
    for c in car_brand:
        s = CarModel.objects.create(name=str(count),
                                    generacion = int(count),
                                    year = year,
                                    brand= c,
                                    engine = str(count))
        count += 1
        car_model.append(s)
    return car_model