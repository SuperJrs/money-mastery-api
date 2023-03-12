from fastapi.testclient import TestClient
from httpx import Response


def test_api_funcionando(client: TestClient, conta_random):
    response: Response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"msg": "A API está no ar!"}
