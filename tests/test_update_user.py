import requests
import json
import jsonschema


def test_update_user_should_be_success(api_url):
    response = requests.put(f'{api_url}/users/2', json={
        "name": "morpheus",
        "job": "zion resident"
    })

    assert response.status_code == 200

    with open('../schemas/update_user.json') as f:
        schema = json.load(f)

    jsonschema.validate(instance=response.json(), schema=schema)
