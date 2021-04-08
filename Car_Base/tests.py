import pytest
from django.urls import reverse

from Car_Base.models import CarBrand, CarModel


def test_check_index(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_car_brand(client, users):
    client.force_login(users[0])
    response = client.get(reverse('add_car_brand'))
    assert response.status_code == 200
    name = "Mazda"
    assert CarBrand.objects.all().count() == 0


@pytest.mark.django_db
def test_car_brand_list(client, car_brand):
    response = client.get(reverse('car_brand_list'))
    assert response.status_code == 200
    car_brand_from_view = response.context['objects_list']
    assert car_brand_from_view.count() == len(car_brand)
    for item in car_brand_from_view:
        assert item in car_brand


@pytest.mark.django_db
def test_add_car_brand_user_not_login(client):
    response = client.get(reverse('add_car_brand'))
    assert response.status_code == 302
    path = response.url.split('?')[0]
    next = response.url.split('?')[1]
    assert path == reverse('login')


@pytest.mark.django_db
def test_add_car_model(client, car_brand, car_model, users):
    client.force_login(users[0])
    response = client.get(reverse('add_car_model'))
    assert response.status_code == 200
    name = 'xd'
    generacion = 1
    year = 1990
    brand = car_brand[0].id
    engine = '1,6 LPG'
    urlconf = car_brand[0].id
    response = client.post(reverse('add_car_model'), {'name': name,
                                                      "generacion": generacion,
                                                      'year': year,
                                                      'brand': brand,
                                                      'engine': engine})

    assert response.status_code == 302
    # assert response.url == reverse('car_list_by_brand', {id : car_brand[0].id})
    # CarModel.objects.get(name=name,
    #                      generacion=generacion,
    #                      year=year,
    #                      brand=car_brand[0],
    #                      engine=engine)
