from fastapi.testclient import TestClient
import json
from httpx import Response
import random
import pytest

from faker import Faker


faker: Faker = Faker()

@pytest.fixture(scope='module')
def reserva_random() -> dict[str, str | float]:
    return {
        'titulo_reserva': faker.text(max_nb_chars=29),
        'descricao_reserva': faker.text(max_nb_chars=99),
    }


def test_post_reserva(client: TestClient, reserva_random: dict[str, str | float], get_token_user_test: str):
    response: Response = client.post(
        '/api/v1/reserva',
        content=json.dumps(reserva_random),
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 201
    
    response_dict = response.json()
    reserva_random.update({
        'cpf_proprietario': response_dict['cpf_proprietario'],
        'id_reserva': response_dict['id_reserva'],
        'dt_criacao': response_dict['dt_criacao']
    })
    
    assert response.json() == reserva_random
    

def test_get_reserva(client: TestClient, reserva_random: dict[str, str | float], get_token_user_test: str):
    response: Response = client.get(
        f'/api/v1/reserva/{reserva_random["id_reserva"]}',
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 200
    assert response.json() == reserva_random


def test_update_reserva(client: TestClient, reserva_random: dict[str, float | str], get_token_user_test: str):
    reserva_random['titulo_reserva'] = faker.text(max_nb_chars=29)
    reserva_random['descricao_reserva'] = faker.text(max_nb_chars=99)
    
    response: Response = client.put(
        f'/api/v1/reserva/{reserva_random["id_reserva"]}', 
        content=json.dumps(reserva_random), 
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 202
    assert response.json() == reserva_random
    
    
def test_delete_reserva(client: TestClient, reserva_random: dict[str, float | str], get_token_user_test: str):
    response: Response = client.delete(
        f'/api/v1/reserva/{reserva_random["id_reserva"]}',
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 202
