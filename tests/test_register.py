import requests
import json
import jsonschema


def test_register_success(api_url):
    response = requests.post(f'{api_url}/register', json={
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })

    assert response.status_code == 200

    with open('../schemas/register.json') as f:
        schema = json.load(f)

    jsonschema.validate(instance=response.json(), schema=schema)


def test_register_without_password_fail(api_url):
    response = requests.post(f'{api_url}/register', json={
        "email": "eve.holt@reqres.in"
    })

    assert response.status_code == 400


def test_register_not_defined_user_fail(api_url):
    response = requests.post(f'{api_url}/register', json={
        "email": "example@gmail.com",
        "password": "example"
    })

    assert response.status_code == 400
