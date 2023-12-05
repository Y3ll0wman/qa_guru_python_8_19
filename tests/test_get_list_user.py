import requests
import jsonschema
import json


def test_get_list_users_should_be_success(api_url):
    response = requests.get(f'{api_url}/users?page=2')

    assert response.status_code == 200
    with open('../schemas/get_list_users.json') as f:
        schema = json.load(f)
    jsonschema.validate(instance=response.json(), schema=schema)
