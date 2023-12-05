import requests
import json
import jsonschema


def test_create_user_should_be_success(api_url):
    response = requests.post(f'{api_url}/users', json={
        "name": "morpheus",
        "job": "leader"
    })

    assert response.status_code == 201

    with open('../schemas/create_user.json') as f:
        schema = json.load(f)

    jsonschema.validate(instance=response.json(), schema=schema)
