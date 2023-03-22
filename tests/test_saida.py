from fastapi.testclient import TestClient
from httpx import Response
import json
from datetime import datetime 
import random
from faker import Faker


faker: Faker = Faker()

def format_timezone_to_datetime(timezone: str) -> str:
    format_dt_time = '%Y-%m-%dT%H:%M:%S'
    timezone_converted = str(datetime.strptime(timezone, format_dt_time))
    return timezone_converted


def test_post_saida(client: TestClient, saida_random: dict[str, float | str], get_token_user_test: str):
    response = client.post(
        '/api/v1/saida',
        content=json.dumps(saida_random),
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    response_dict: dict = response.json()
    
    saida_random.update(
        {
            'cpf_proprietario': response_dict['cpf_proprietario'], 
            'id_saida': response_dict['id_saida']
        }
    )
    response_dict['dt_hora_saida'] = format_timezone_to_datetime(response_dict['dt_hora_saida'])
    
    assert response.status_code == 201
    assert response_dict == saida_random
    
    
def test_get_saida(client: TestClient, saida_random: dict[str, float | str], get_token_user_test: str):
    response: Response = client.get(
        f'/api/v1/saida/{saida_random["id_saida"]}',
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    response_dict = response.json()
    response_dict['dt_hora_saida'] = format_timezone_to_datetime(response_dict['dt_hora_saida'])
    
    assert response.status_code == 200
    assert response_dict == saida_random


def test_update_saida(client: TestClient, saida_random: dict[str, float | str], get_token_user_test: str):
    saida_random['valor_saida'] = round(random.uniform(2,2000), 2)
    saida_random['descricao_saida'] = faker.pystr()
    
    response: Response = client.put(
        f'/api/v1/saida/{saida_random["id_saida"]}', 
        content=json.dumps(saida_random), 
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    response_dict = response.json()
    response_dict['dt_hora_saida'] = format_timezone_to_datetime(response_dict['dt_hora_saida'])
    
    assert response.status_code == 202
    assert response_dict['valor_saida'] == saida_random['valor_saida']
    assert response_dict['descricao_saida'] == saida_random['descricao_saida']
    

def test_delete_saida(client: TestClient, saida_random: dict[str, float | str], get_token_user_test: str):
    response: Response = client.delete(
        f'/api/v1/saida/{saida_random["id_saida"]}',
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 202
