import pytest
from django.test import Client
from django.contrib.auth.models import User, Permission

from .models import Types, Workers


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
def types():
    type = []
    for x in range(1, 11):
        u = Types.objects.create(name=str(x))
        type.append(u)
    return type

@pytest.fixture
def workers(types):
    count = 1

    worker = []
    for t in types:
        w = Workers.objects.create(name=str(count),
                                    price = int(count),
                                    type= t,
                                    work = str(count))
        count += 1
        worker.append(w)
    return worker