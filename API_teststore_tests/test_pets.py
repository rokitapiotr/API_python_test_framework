from utils.utils import getAPIData

BASE_URI = 'https://petstore.swagger.io/v2/pet/'
pet_ID = '151'


def test_getPetById_response():
    url = BASE_URI + pet_ID
    data, resp_status, time_taken = getAPIData(url)
    assert data['id'] == int(pet_ID)
    assert resp_status == 200
    print('Time taken ', time_taken)
