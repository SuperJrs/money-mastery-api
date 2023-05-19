from fastapi.testclient import TestClient
import json
from httpx import Response
import random
import pytest

from faker import Faker


faker: Faker = Faker()

@pytest.fixture(scope='module')
def gasto_random() -> dict[str, str | float]:
    return {
        'titulo_gasto': faker.text(max_nb_chars=29),
        'valor_gasto': round(random.uniform(2,2000), 2),
    }


def test_post_gasto_base(client: TestClient, gasto_random: dict[str, str | float], get_token_user_test: str):
    response: Response = client.post(
        '/api/v1/gasto-base',
        content=json.dumps(gasto_random),
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 201
    
    response_dict = response.json()
    gasto_random.update({
        'cpf_proprietario': response_dict['cpf_proprietario'],
        'id_gasto_base': response_dict['id_gasto_base']
    })
    
    assert response.json() == gasto_random
    

def test_get_gasto_base(client: TestClient, gasto_random: dict[str, str | float], get_token_user_test: str):
    response: Response = client.get(
        f'/api/v1/gasto-base/{gasto_random["id_gasto_base"]}',
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 200
    assert response.json() == gasto_random


def test_update_gasto_base(client: TestClient, gasto_base_random: dict[str, float | str], get_token_user_test: str):
    gasto_base_random['titulo_gasto'] = faker.text(max_nb_chars=29)
    gasto_base_random['valor_gasto'] = round(random.uniform(2,2000), 2)
    
    response: Response = client.put(
        f'/api/v1/gasto-base/{gasto_base_random["id_gasto_base"]}', 
        content=json.dumps(gasto_base_random), 
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 202
    assert response.json() == gasto_base_random
    
def test_delete_gasto_base(client: TestClient, gasto_base_random: dict[str, float | str], get_token_user_test: str):
    response: Response = client.delete(
        f'/api/v1/gasto-base/{gasto_base_random["id_gasto_base"]}',
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 202
