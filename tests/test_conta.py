from faker import Faker
from fastapi.testclient import TestClient
from httpx import Response
from urllib.parse import urlencode
from typing import Any
import json, random

import pytest

faker: Faker = Faker()


def test_post_conta(client: TestClient, conta_random: dict[str, Any], conta_sem_senha: dict[str, Any]):    
    response: Response = client.post('/api/v1/user/register', content=json.dumps(conta_random))
    
    assert response.status_code == 201
    assert response.json() == conta_sem_senha
    

def test_get_conta_by_cpf(client: TestClient, conta_sem_senha: dict[str, Any]):
    response: Response = client.get(f'/api/v1/conta/{conta_sem_senha["cpf_proprietario"]}')

    assert response.status_code == 200
    assert response.json() == conta_sem_senha


def test_login_in_conta(client: TestClient, conta_random: dict[str, Any]):
    form_data: bytes = urlencode({
        'username': conta_random['email'],
        'password': conta_random['senha']
    }).encode('utf-8')
    
    response: Response = client.post(
        '/api/v1/user/login', 
        content=form_data.decode(),
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    
    assert response.status_code == 200
    assert 'access_token' in response.json()


def test_me_conta(client: TestClient, conta_sem_senha: dict[str, Any], get_token: str):
    response: Response = client.get(
        '/api/v1/user/me', 
        headers={'Authorization': f'Bearer {get_token}'}
    )
    
    assert response.status_code == 200
    assert response.json() == conta_sem_senha
    
    
def test_update_all_args_conta(client: TestClient, get_token: str, conta_sem_senha: dict[str, Any]):
    data_update: dict[str, Any] = dict(
        nome_proprietario = faker.name(),
        dt_nasc_proprietario = str(faker.date_between(
                start_date='-100y', end_date='-18y'
            )),
        telefone = random.randint(10000000000, 99999999999)
    )
    
    response: Response = client.put(
        '/api/v1/user',
        headers={'Authorization': f'Bearer {get_token}'},
        content=json.dumps(data_update)
    )
    conta_sem_senha.update(**data_update)
    
    assert response.status_code == 202
    assert response.json() == conta_sem_senha
    
    
@pytest.mark.skip
def test_update_nome_proprietario_conta(client: TestClient, get_token: str, conta_sem_senha: dict[str, Any]):
    data_update: dict[str, str] = dict(nome_proprietario = faker.name())
    
    response: Response = client.put(
        '/api/v1/user',
        headers={'Authorization': f'Bearer {get_token}'},
        content=json.dumps(data_update)
    )
    conta_sem_senha.update(**data_update) 
    
    assert response.status_code == 202   
    assert response.json() == conta_sem_senha


@pytest.mark.skip
def test_update_dt_nasc_and_telefone_conta(client: TestClient, get_token: str, conta_sem_senha: dict[str, Any]):
    data_update: dict[str, Any] = dict(
        dt_nasc_proprietario = str(faker.date_between(
                start_date='-100y', end_date='-18y'
            )),
        telefone = random.randint(10000000000, 99999999999)
    )
    
    response: Response = client.put(
        '/api/v1/user',
        headers={'Authorization': f'Bearer {get_token}'},
        content=json.dumps(data_update)
    )
    conta_sem_senha = dict(conta_sem_senha, **data_update) 
    
    assert response.status_code == 202
    assert response.json() == conta_sem_senha


def test_delete_me_conta(client: TestClient, get_token: str):
    response: Response = client.delete(
        '/api/v1/user', headers={'Authorization': f'Bearer {get_token}'}
    )

    assert response.status_code == 202
    assert response.json() == dict(msg='Conta apagada com sucesso!')


@pytest.mark.skip
def test_me_conta_after_deleting(client: TestClient, get_token: str):
    response: Response = client.get(
        '/api/v1/user/me', 
        headers={'Authorization': f'Bearer {get_token}'}
    )
    
    assert response.status_code == 404
    assert response.json() == dict(detail='Conta não encontrada!')
    