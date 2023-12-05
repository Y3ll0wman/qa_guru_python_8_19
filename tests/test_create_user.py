from utils.load_schema import load_schema

import requests
import jsonschema


def test_create_user_should_be_success(api_url):
    # GIVEN
    schema = load_schema('../json_schemas/create_user.json')

    # WHEN
    response = requests.post(f'{api_url}/users', json={
        "name": "morpheus",
        "job": "leader"
    })

    # THEN
    assert response.status_code == 201
    jsonschema.validate(instance=response.json(), schema=schema)
