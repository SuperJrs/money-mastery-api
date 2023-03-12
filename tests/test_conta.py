from faker import Faker
from fastapi.testclient import TestClient
from httpx import Response
from urllib.parse import urlencode
from typing import Any
import json

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
    