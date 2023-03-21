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

def test_add_entrada(client: TestClient, entrada_random: dict[str, float | str], get_token_user_test: str):    
    response: Response = client.post(
        '/api/v1/entrada', 
        content=json.dumps(entrada_random), 
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    response_dict = response.json()
    
    entrada_random.update(
        {
            'cpf_proprietario': response_dict['cpf_proprietario'], 
            'id_entrada': response_dict['id_entrada']
         }
    )    
    response_dict['dt_hora_entrada'] = format_timezone_to_datetime(response_dict['dt_hora_entrada'])
    
    assert response.status_code == 201
    assert response_dict == entrada_random
    

def test_get_entrada(client: TestClient, entrada_random: dict[str, float | str], get_token_user_test: str):
    response: Response = client.get(
        f'/api/v1/entrada/{entrada_random["id_entrada"]}',
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    response_dict = response.json()
    response_dict['dt_hora_entrada'] = format_timezone_to_datetime(response_dict['dt_hora_entrada'])
    
    assert response.status_code == 200
    assert response_dict == entrada_random
    

def test_update_entrada(client: TestClient, entrada_random: dict[str, float | str], get_token_user_test: str):
    entrada_random['valor_entrada'] = round(random.uniform(2,2000), 2)
    entrada_random['descricao_entrada'] = faker.pystr()
    
    response: Response = client.put(
        f'/api/v1/entrada/{entrada_random["id_entrada"]}', 
        content=json.dumps(entrada_random), 
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    response_dict = response.json()
    response_dict['dt_hora_entrada'] = format_timezone_to_datetime(response_dict['dt_hora_entrada'])
    
    assert response.status_code == 202
    assert response_dict['valor_entrada'] == entrada_random['valor_entrada']
    assert response_dict['descricao_entrada'] == entrada_random['descricao_entrada']
    

def test_delete_entrada(client: TestClient, entrada_random: dict[str, float | str], get_token_user_test: str):
    response: Response = client.delete(
        f'/api/v1/entrada/{entrada_random["id_entrada"]}',
        headers={'Authorization': f'Bearer {get_token_user_test}'}
    )
    
    assert response.status_code == 202
