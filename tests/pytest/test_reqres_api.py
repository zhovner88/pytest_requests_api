import requests
import time

API_URL = 'https://reqres.in/api/users'
API_KEY_HEADER = {"x-api-key": "reqres-free-v1"}

###### LIST USERS #######################
###### https://reqres.in/api/users?page=#

def test_list_users_page_1():
    # Positive: Check that page 1 returns 6 users
    response = requests.get(f'{API_URL}?page=1', headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert isinstance(data['data'], list)
    assert len(data['data']) == 6


def test_list_users_nonexistent_page():
    # Negative: Non-existent page should return an empty list
    response = requests.get(f'{API_URL}?page=999', headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert isinstance(data['data'], list)
    assert len(data['data']) == 0


def test_list_users_no_page_param():
    # Edge case: No page param should return first page
    response = requests.get(API_URL, headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert 'page' in data
    assert data['page'] == 1
    assert 'data' in data
    assert isinstance(data['data'], list)
    assert len(data['data']) == 6

# TEST FAILS
def test_list_users_no_api_key():
    # Security/Negative: No API key header should return 403 or 401
    response = requests.get(f'{API_URL}?page=1')
    assert response.status_code in (401, 403)


def test_list_users_with_delay():
    # Performance: Response with delay param should take at least 3 seconds
    start = time.time()
    response = requests.get(f'{API_URL}?page=1&delay=3', headers=API_KEY_HEADER)
    elapsed = time.time() - start
    assert response.status_code == 200
    assert elapsed >= 3 

###### SINGLE USER ###############
# https://reqres.in/api/users/<id> #

def test_single_user_exists():
    # Positive: Check that a valid user (id=2) returns correct data
    response = requests.get(f'{API_URL}/2', headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    user = data['data']
    assert user['id'] == 2
    assert 'email' in user
    assert 'first_name' in user
    assert 'last_name' in user
    assert 'avatar' in user
    assert 'support' in data
    assert 'url' in data['support']
    assert 'text' in data['support']


def test_single_user_not_found():
    # Negative: Non-existent user (id=23) should return 404
    response = requests.get(f'{API_URL}/23', headers=API_KEY_HEADER)
    assert response.status_code == 404
    data = response.json()
    assert data == {}


def test_single_user_invalid_id():
    # Edge case: Invalid user id (string instead of int) should return 404
    response = requests.get(f'{API_URL}/abc', headers=API_KEY_HEADER)
    assert response.status_code == 404
    data = response.json()
    assert data == {}

###### LIST RESOURCES ###############
# https://reqres.in/api/unknown #

def test_list_resources():
    # Positive: Check that the resource list returns 6 items on page 1
    response = requests.get('https://reqres.in/api/unknown', headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    resources = data['data']
    assert isinstance(resources, list)
    assert len(resources) == 6
    for resource in resources:
        assert 'id' in resource
        assert 'name' in resource
        assert 'year' in resource
        assert 'color' in resource
        assert 'pantone_value' in resource
    assert 'support' in data
    assert 'url' in data['support']
    assert 'text' in data['support']


def test_list_resources_nonexistent_page():
    # Negative: Non-existent page should return an empty list
    response = requests.get('https://reqres.in/api/unknown?page=999', headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert isinstance(data['data'], list)
    assert len(data['data']) == 0


def test_list_resources_no_page_param():
    # Edge case: No page param should return first page
    response = requests.get('https://reqres.in/api/unknown', headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert 'page' in data
    assert data['page'] == 1
    assert 'data' in data
    assert isinstance(data['data'], list)
    assert len(data['data']) == 6

###### SINGLE RESOURCE ###############
# https://reqres.in/api/unknown/<id> #

def test_single_resource_exists():
    # Positive: Check that a valid resource (id=2) returns correct data
    response = requests.get('https://reqres.in/api/unknown/2', headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    resource = data['data']
    assert resource['id'] == 2
    assert 'name' in resource
    assert 'year' in resource
    assert 'color' in resource
    assert 'pantone_value' in resource
    assert 'support' in data
    assert 'url' in data['support']
    assert 'text' in data['support']


def test_single_resource_not_found():
    # Negative: Non-existent resource (id=23) should return 404
    response = requests.get('https://reqres.in/api/unknown/23', headers=API_KEY_HEADER)
    assert response.status_code == 404
    data = response.json()
    assert data == {}


def test_single_resource_invalid_id():
    # Edge case: Invalid resource id (string instead of int) should return 404
    response = requests.get('https://reqres.in/api/unknown/abc', headers=API_KEY_HEADER)
    assert response.status_code == 404
    data = response.json()
    assert data == {}

###### LIST USERS (PAGE 1) ###############
# https://reqres.in/api/users #

def test_list_users_page_1_again():
    # Positive: Check that the user list returns 6 users on page 1
    response = requests.get('https://reqres.in/api/users', headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    users = data['data']
    assert isinstance(users, list)
    assert len(users) == 6
    for user in users:
        assert 'id' in user
        assert 'email' in user
        assert 'first_name' in user
        assert 'last_name' in user
        assert 'avatar' in user
    assert 'support' in data
    assert 'url' in data['support']
    assert 'text' in data['support']


def test_list_users_nonexistent_page_again():
    # Negative: Non-existent page should return an empty list
    response = requests.get('https://reqres.in/api/users?page=999', headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data
    assert isinstance(data['data'], list)
    assert len(data['data']) == 0


def test_list_users_no_page_param_again():
    # Edge case: No page param should return first page
    response = requests.get('https://reqres.in/api/users', headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert 'page' in data
    assert data['page'] == 1
    assert 'data' in data
    assert isinstance(data['data'], list)
    assert len(data['data']) == 6

###### CREATE USER (POST) ###############
# https://reqres.in/api/users #

def test_create_user_success():
    # Positive: Create a user with valid data
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post('https://reqres.in/api/users', json=payload, headers=API_KEY_HEADER)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "morpheus"
    assert data["job"] == "leader"
    assert "id" in data
    assert "createdAt" in data


def test_create_user_missing_fields():
    # Negative: Create a user with missing required fields (e.g., no job)
    payload = {"name": "morpheus"}
    response = requests.post('https://reqres.in/api/users', json=payload, headers=API_KEY_HEADER)
    # The API still creates the user, but job will be missing in response
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "morpheus"
    assert "job" not in data or data["job"] is None
    assert "id" in data
    assert "createdAt" in data

###### UPDATE USER (PUT) ###############
# https://reqres.in/api/users/2 #

def test_update_user_success():
    # Positive: Update a user with valid data
    payload = {"name": "morpheus", "job": "zion resident"}
    response = requests.put('https://reqres.in/api/users/2', json=payload, headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "morpheus"
    assert data["job"] == "zion resident"
    assert "updatedAt" in data


def test_update_user_missing_fields():
    # Negative: Update a user with missing required fields (e.g., no job)
    payload = {"name": "morpheus"}
    response = requests.put('https://reqres.in/api/users/2', json=payload, headers=API_KEY_HEADER)
    # The API still updates the user, but job will be missing in response
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "morpheus"
    assert "job" not in data or data["job"] is None
    assert "updatedAt" in data

###### PARTIAL UPDATE USER (PATCH) ###############
# https://reqres.in/api/users/2 #

def test_partial_update_user_success():
    # Positive: Partially update a user with valid data (PATCH)
    payload = {"job": "matrix operator"}
    response = requests.patch('https://reqres.in/api/users/2', json=payload, headers=API_KEY_HEADER)
    assert response.status_code == 200
    data = response.json()
    assert data["job"] == "matrix operator"
    assert "updatedAt" in data


def test_partial_update_user_missing_fields():
    # Negative: Partially update a user with no data (PATCH)
    payload = {}
    response = requests.patch('https://reqres.in/api/users/2', json=payload, headers=API_KEY_HEADER)
    # The API still returns 200 and only updatedAt
    assert response.status_code == 200
    data = response.json()
    assert "updatedAt" in data

###### DELETE USER ###############
# https://reqres.in/api/users/2 #

def test_delete_user_success():
    # Positive: Delete a user (DELETE)
    response = requests.delete('https://reqres.in/api/users/2', headers=API_KEY_HEADER)
    assert response.status_code == 204
    assert response.text == ""