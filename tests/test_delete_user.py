import requests


def test_delete_user_should_be_success(api_url):
    response = requests.delete(f'{api_url}/users/2')

    assert response.status_code == 204
