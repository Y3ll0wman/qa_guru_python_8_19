from utils.load_schema import load_schema

import requests
import jsonschema


def test_update_user_should_be_success(api_url):
    # GIVEN
    schema = load_schema('../json_schemas/update_user.json')

    # WHEN
    response = requests.put(f'{api_url}/users/2', json={
        "name": "morpheus",
        "job": "zion resident"
    })

    # THEN
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=schema)
