from utils.load_schema import load_schema

import requests
import jsonschema


def test_register_success(api_url):
    # GIVEN
    schema = load_schema('../json_schemas/register.json')

    # WHEN
    response = requests.post(f'{api_url}/register', json={
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })

    # THEN
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=schema)


def test_register_without_password_fail(api_url):
    # WHEN
    response = requests.post(f'{api_url}/register', json={
        "email": "eve.holt@reqres.in"
    })

    # THEN
    assert response.status_code == 400


def test_register_not_defined_user_fail(api_url):
    # WHEN
    response = requests.post(f'{api_url}/register', json={
        "email": "example@gmail.com",
        "password": "example"
    })

    # THEN
    assert response.status_code == 400
