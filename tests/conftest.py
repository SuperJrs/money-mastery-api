from fastapi.testclient import TestClient
from faker import Faker
from typing import Any, Generator
from urllib.parse import urlencode
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

import pytest, copy, random

from money_mastery.main import app
from money_mastery.core.database import settings_db
from money_mastery.models.conta_model import Conta
from money_mastery.core.configs import settings


faker: Faker = Faker()


@pytest.fixture(scope='module')
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c
        
        
@pytest.fixture(scope='session')
def db() -> Generator:
    engine = create_engine(settings_db.DB_URL_SYNC)
    Session: sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    with Session() as sess:
        yield sess   


@pytest.fixture(scope='module')
def conta_random() -> dict[str, Any]:
    conta_random: dict[str, Any] = dict(
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
def conta_sem_senha(conta_random: dict[str, Any]) -> dict[str, Any]:
    clone_conta: dict[str, Any] = copy.deepcopy(conta_random)
    del clone_conta['senha']
    return clone_conta


@pytest.fixture(scope='module')
def get_token(client: TestClient, conta_random: dict[str, Any]) -> str:
    form_data: bytes = urlencode({
        'username': conta_random['email'],
        'password': conta_random['senha']
    }).encode('utf-8')
    
    response: dict[str, str] = client.post(
        '/api/v1/user/login', 
        content=form_data.decode(),
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    ).json()

    return response['access_token']


@pytest.fixture(scope='module')
def get_token_user_test(client: TestClient):
    form_data: bytes = urlencode({
        'username': settings.EMAIL_TEST_USER,
        'password': settings.PASSWORD_TEST_USER
    }).encode('utf-8')
    
    response: dict[str, str] = client.post(
        '/api/v1/user/login', 
        content=form_data.decode(),
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    ).json()

    return response['access_token']


@pytest.fixture(scope='module')
def entrada_random() -> dict[str, float | str]:    
    origens: list[str] = ['PIX', 'SALARIO', 'EMPRESTIMO', 'RESERVA', 'OUTRO']
    new_entrada: dict[str, float | str] = dict(
        valor_entrada=round(random.uniform(2,2000), 2),
        origem=random.choices(origens)[0],
        descricao_entrada=faker.pystr(),
        dt_hora_entrada=str(faker.date_time_between(start_date='-5y', end_date='+1y')),
        id_reserva=None,
        id_emprestimo=None
    ) # type: ignore
    
    return new_entrada


@pytest.fixture(scope='module')
def saida_random() -> dict[str, float | str]:    
    categorias: list[str] = ['LAZER', 'ALIMENTACAO', 'SAUDE', 'MORADIA', 'TRANSPORTE', 'EDUCACAO', 'OUTRO']
    formas_pagamento: list[str] = ['CREDITO', 'DEBITO', 'PIX', 'DINHEIRO', 'RESERVA', 'EMPRESTIMO']
    new_entrada: dict[str, float | str] = dict(
        valor_saida=round(random.uniform(2,2000), 2),
        categoria=random.choices(categorias)[0],
        descricao_saida=faker.pystr(),
        dt_hora_saida=str(faker.date_time_between(start_date='-5y', end_date='+1y')),
        forma_pagamento=random.choices(formas_pagamento)[0],
        id_reserva=None
    ) # type: ignore
    
    return new_entrada
