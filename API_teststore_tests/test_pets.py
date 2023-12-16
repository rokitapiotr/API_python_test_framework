from utils.utils import getAPIData, putData, deleteData
from utils.confparser import *

pet_ID = '171'
BASE_URI = getPetAPIurl()


def test_getPetById_response():
    url = BASE_URI + pet_ID
    data, resp_status, time_taken = getAPIData(url)
    assert data['id'] == int(pet_ID)
    assert resp_status == 200
    print('Time taken ', time_taken)


def test_updating_Pet():
    payload = {'id': int(pet_ID), "name": "Cutie", "stats": "pending"}
    data, resp_status, time_taken = putData(BASE_URI, payload)
    assert data['id'] == int(pet_ID)
    print(data)


def test_delete_PetByID():
    url = BASE_URI + pet_ID
    api_key = {'api_key': 'apiKeys123'}
    data, resp_status, time_taken = deleteData(url, api_key)
    assert data['message'] == pet_ID
    assert resp_status == 200
