from faker import Faker
import json
from urllib.parse import urlencode

faker = Faker()


def test_post_conta(client, conta_random, conta_sem_senha):
    response = client.post('/api/v1/user/register', content=json.dumps(conta_random))
    
    assert response.status_code == 201
    assert response.json() == conta_sem_senha
    

def test_get_conta_by_cpf(client, conta_sem_senha):
    response = client.get(f'/api/v1/conta/{conta_sem_senha["cpf_proprietario"]}')

    assert response.status_code == 200
    assert response.json() == conta_sem_senha


def test_login_in_conta(client, conta_random):
    form_data = urlencode({
        'username': conta_random['email'],
        'password': conta_random['senha']
    }).encode('utf-8')
    
    response = client.post(
        '/api/v1/user/login', 
        content=form_data.decode(),
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    
    assert response.status_code == 200
    assert 'access_token' in response.json()


def test_me_conta(client, conta_sem_senha, get_token):
    response = client.get(
        '/api/v1/user/me', 
        headers={'Authorization': f'Bearer {get_token}'}
    )
    
    assert response.status_code == 200
    assert response.json() == conta_sem_senha
    