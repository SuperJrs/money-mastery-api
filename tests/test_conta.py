from faker import Faker
import json
import random
from typing import Any

from money_mastery.schemas.conta_schema import ContaSchema
from .conftest import test_app


faker = Faker()

conta_random: dict['str', Any] = dict(
    cpf_proprietario = random.randint(10000000000, 99999999999),
    nome_proprietario = faker.name(),
    dt_nasc_proprietario = str(faker.date_between(start_date='-100y', end_date='-18y')),
    telefone = random.randint(10000000000, 99999999999),
    email = faker.email(),
    senha = faker.password()
)


def test_post_conta(test_app):
    response = test_app.post('/conta', content=json.dumps(conta_random))
    
    assert response.status_code == 201
    assert response.json() == conta_random
    

def test_get_conta_by_cpf(test_app):
    print(f'/conta/{conta_random["cpf_proprietario"]}')
    response = test_app.get(f'/conta/{conta_random["cpf_proprietario"]}')
    
    assert response.status_code == 200
    assert response.json() == conta_random
    