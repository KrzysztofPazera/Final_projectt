import pytest
from django.test import Client
from django.contrib.auth.models import User, Permission

from Car_Base.models import CarBrand, CarModel, PartsCategory, CarParts

@pytest.fixture(autouse=True)
def _use_static_files_storage(settings):
    settings.STATICFILES_STORAGE = (
        "django.contrib.staticfiles.storage.StaticFilesStorage"
    )

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

@pytest.fixture
def part_category():
    part_category = []
    for x in range(1, 11):
        u = PartsCategory.objects.create(name=str(x))
        part_category.append(u)
    return part_category

@pytest.fixture
def parts(part_category,car_model):
    cars_models=car_model
    count = 1
    id_number_of_product = 111
    parts = []
    for c in part_category:
        for m in cars_models:
            c = CarParts.objects.create(name=str(count),
                                    id_number_of_product = str(id_number_of_product),
                                    category = c,
                                    car_model= m,
                                    price = int(count))
        count += 1
        parts.append(c)
    return parts