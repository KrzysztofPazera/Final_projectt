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
    client.post(reverse("add_car_brand"), {'name': name})
    assert CarBrand.objects.all().count() == 1
    CarBrand.objects.get(name=name)


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
    assert response.url == reverse('car_brand_list')
    assert CarModel.objects.filter(name=name,
                         generacion=generacion,
                         year=year,
                         brand=car_brand[0],
                         engine=engine).count()==1


@pytest.mark.django_db
def test_add_car_brand(client, users):
    client.force_login(users[0])
    response = client.get(reverse('add_car_brand'))
    assert response.status_code == 200
    name = "Mazda"
    assert CarBrand.objects.all().count() == 0
    client.post(reverse("add_car_brand"), {'name': name})
    assert CarBrand.objects.all().count() == 1
    CarBrand.objects.get(name=name)

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
    assert response.url == reverse('car_brand_list')
    assert CarModel.objects.filter(name=name,
                         generacion=generacion,
                         year=year,
                         brand=car_brand[0],
                         engine=engine).count()==1

@pytest.mark.django_db
def test_models_list(client, car_brand, car_model):
    brand_id= car_brand[0].id
    response = client.get(reverse('car_list_by_brand', args=[brand_id]))
    assert response.status_code ==200


@pytest.mark.django_db
def test_parts_list(client, part_category, parts):
    category_id= part_category[0].id
    response = client.get(reverse('parts_list', args=[category_id]))
    assert response.status_code ==200
    parts_from_view = response.context['objects_list']
    assert parts_from_view.count() == len(parts)
    for item in parts_from_view:
        assert item in parts

@pytest.mark.django_db
def test_add_parts_category(client, users):
    client.force_login(users[0])
    response = client.get(reverse('add_category_of_parts'))
    assert response.status_code == 200
    name = "Maska"
    assert CarBrand.objects.all().count() == 0

@pytest.mark.django_db
def test_parts_list(client, part_category):
    response = client.get(reverse('parts_category'))
    assert response.status_code == 200
    parts_category_from_view = response.context['objects_list']
    assert parts_category_from_view.count() == len(part_category)
    for item in parts_category_from_view:
        assert item in part_category



@pytest.mark.django_db
def test_add_car_model(client, users):
    client.force_login(users[0])
    response = client.get(reverse('add_car_part'))
    assert response.status_code == 200
    # name = 'xd'
    # car_model = car_model[0].id
    # id_number_of_product = 1111
    # category = part_category[0].id
    # price = 1
    # urlconf = car_model[0].id
    # response = client.post(reverse('add_car_part'), {'name': name,
    #                                                   "car_model": car_model,
    #                                                   'id_number_of_product': id_number_of_product,
    #                                                   'category': category,
    #                                                   'price': price})
    # assert response.status_code == 302