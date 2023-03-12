from fastapi.testclient import TestClient
from faker import Faker
from typing import Any, Generator
from urllib.parse import urlencode

import pytest, copy, random

from money_mastery.main import app


faker = Faker()


@pytest.fixture(scope='module')
def client() -> Generator[TestClient, None, None]:
    teste = TestClient(app)
    # teste.get(auth=)
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope='module')
def conta_random():
    conta_random: dict['str', Any] = dict(
        cpf_proprietario = random.randint(10000000000, 99999999999),
        nome_proprietario = faker.name(),
        dt_nasc_proprietario = str(faker.date_between(
                start_date='-100y', end_date='-18y'
            )),
        telefone = random.randint(10000000000, 99999999999),
        email = faker.email(),
        senha = faker.password()
    )
    return conta_random


@pytest.fixture
def conta_sem_senha(conta_random):
    clone_conta = copy.deepcopy(conta_random)
    del clone_conta['senha']
    return clone_conta


@pytest.fixture(scope='module')
def get_token(client, conta_random):
    form_data = urlencode({
        'username': conta_random['email'],
        'password': conta_random['senha']
    }).encode('utf-8')
    
    response = client.post(
        '/api/v1/user/login', 
        content=form_data.decode(),
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    ).json()

    return response['access_token']
