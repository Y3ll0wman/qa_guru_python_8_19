import requests
import json
import jsonschema


def test_get_user_should_be_success(api_url):
    response = requests.get(f'{api_url}/users/2')

    assert response.status_code == 200

    with open('../schemas/get_user.json') as f:
        schema = json.load(f)

    jsonschema.validate(instance=response.json(), schema=schema)


def test_get_user_should_be_fail(api_url):
    response = requests.get(f'{api_url}/users/www')

    assert response.status_code == 404
