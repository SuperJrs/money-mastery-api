from fastapi.testclient import TestClient
import json
from httpx import Response
import random
import pytest

from faker import Faker


faker: Faker = Faker()

@pytest.fixture(scope='module')
def lembrete_random() -> dict[str, str | float]:
    return {
        'titulo_lembrete': faker.text(max_nb_chars=29),
        'dt_lembrete': faker.date_between(start_date='today', end_date='+1y'),
    }


def test_post_lembrete(client: TestClient, lembrete_random: dict[str, str | float], get_token_user_test: str):
    response: Response = client.post(
        '/api/v1/lembrete',
        content=json.dumps(lembrete_random),
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 201
    
    response_dict = response.json()
    lembrete_random.update({
        'cpf_proprietario': response_dict['cpf_proprietario'],
        'id_lembrete': response_dict['id_lembrete']
    })
    
    assert response.json() == lembrete_random
    

def test_get_lembrete(client: TestClient, lembrete_random: dict[str, str | float], get_token_user_test: str):
    response: Response = client.get(
        f'/api/v1/lembrete/{lembrete_random["id_lembrete"]}',
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 200
    assert response.json() == lembrete_random


def test_update_lembrete(client: TestClient, lembrete_random: dict[str, float | str], get_token_user_test: str):
    lembrete_random['titulo_lembrete'] = faker.text(max_nb_chars=29)
    lembrete_random['dt_lembrete'] = faker.date_between(start_date='today', end_date='+1y')
    
    response: Response = client.put(
        f'/api/v1/lembrete/{lembrete_random["id_lembrete"]}', 
        content=json.dumps(lembrete_random), 
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 202
    assert response.json() == lembrete_random
    
    
def test_delete_lembrete(client: TestClient, lembrete_random: dict[str, float | str], get_token_user_test: str):
    response: Response = client.delete(
        f'/api/v1/lembrete/{lembrete_random["id_lembrete"]}',
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 202
