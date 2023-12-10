import requests
import json

BASE_URI = 'https://petstore.swagger.io/v2/pet/'
pet_ID = '151'


def test_getPetById_response():
    url = BASE_URI + pet_ID
    header = {
        'Content-Type': 'application/json'
    }
    print(url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    print(json.dumps(data, indent=3))
    assert len(data) > 0, "empty response"


# testing response body for 'ID' key

def test_getPetById_id():
    url = BASE_URI + pet_ID
    header = {
        'Content-Type': 'application/json'
    }
    print(url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    assert data['id'] == 151


def test_addNewPet():
    url = BASE_URI
    header = {
        'Content-Type': 'application/json'
    }
    payload = {
        'id': 191,
        'name': 'Cutie',
        'status': 'available'
    }
    response = requests.post(url, verify=False, json=payload, headers=header)
    data = response.json()
    assert data['id'] == 191
    assert len(data) > 0, "empty response"
