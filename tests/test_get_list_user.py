from utils.load_schema import load_schema

import requests
import jsonschema


def test_get_list_users_should_be_success(api_url):
    # GIVEN
    schema = load_schema('../json_schemas/get_list_users.json')

    # WHEN
    response = requests.get(f'{api_url}/users?page=2')

    # THEN
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=schema)
