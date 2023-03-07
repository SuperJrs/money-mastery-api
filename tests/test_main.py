def test_api_funcionando(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"msg": "A API está no ar!"}
