import requests


def test_delete_user_should_be_success(api_url):
    # WHEN
    response = requests.delete(f'{api_url}/users/2')

    # THEN
    assert response.status_code == 204
