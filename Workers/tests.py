from django.test import TestCase
import pytest
from django.urls import reverse
from .models import Types, Workers
# Create your tests here.
@pytest.mark.django_db
def test_add_type(client, users):
    client.force_login(users[0])
    response = client.get(reverse('add_type_work'))
    assert response.status_code == 200
    assert Types.objects.all().count() == 0
    name = "xd"
    client.post(reverse("add_type_work"), {'name': name})
    assert Types.objects.all().count() == 1
    Types.objects.get(name=name)

@pytest.mark.django_db
def test_tye_list(client, types):
    response = client.get(reverse('type_work_list'))
    assert response.status_code == 200
    type_from_view = response.context['types']
    assert type_from_view.count() == len(types)
    for item in type_from_view:
        assert item in types

@pytest.mark.django_db
def test_add_worker(users,client, types, workers):
    client.force_login(users[0])
    response = client.get(reverse('add_worker'))
    assert response.status_code == 200
    name = "xd"
    price = '1'
    type = types[0].id
    work = 'xd'
    urlconf = types[0].id

    response=client.post(reverse("add_worker"), {'name': name,
                                        'type': type,
                                        'price':price,
                                        'work':work})
    assert response.status_code == 302
    assert Workers.objects.filter(name=name)

@pytest.mark.django_db
def test_types_list(client, types):
    response = client.get(reverse('type_work_list'))
    assert response.status_code == 200
    types_from_view = response.context['types']
    assert types_from_view.count() == len(types)
    for item in types_from_view:
        assert item in types

@pytest.mark.django_db
def test_workers_list(client, types, workers):
    type_id= types[0].id
    response = client.get(reverse('worker_list_by_type', args=[type_id]))
    assert response.status_code ==200
