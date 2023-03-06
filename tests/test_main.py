from .conftest import test_app


def test_api_funcionando(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "A API está no ar!"}
