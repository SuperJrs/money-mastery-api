from faker import Faker
import json
import random
from typing import Any


faker = Faker()

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


def test_post_conta(client):
    response = client.post('/conta', content=json.dumps(conta_random))
    
    assert response.status_code == 201
    assert response.json() == conta_random
    

def test_get_conta_by_cpf(client):
    response = client.get(f'/conta/{conta_random["cpf_proprietario"]}')
    
    assert response.status_code == 200
    assert response.json() == conta_random
