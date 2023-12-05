from utils.load_schema import load_schema

import requests
import jsonschema


def test_get_user_should_be_success(api_url):
    # GIVEN
    schema = load_schema('../json_schemas/get_user.json')
    user_id = 2

    # WHEN
    response = requests.get(f'{api_url}/users/{user_id}')

    # THEN
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=schema)


def test_get_user_should_be_fail(api_url):
    # GIVEN
    user_id = 'www'

    # WHEN
    response = requests.get(f'{api_url}/users/{user_id}')

    # THEN
    assert response.status_code == 404
