import json
import pytest
from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.confparser import getFlaskAppBaseURL

#loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
#loginURLPath = '/login'
usersUrlPath = '/users'


#@pytest.fixture
#def get_token():
    #loginURL = baseURI + loginURLPath
    #payload = getJsonFromFile(loginJsonFile)
    #response = postApiData(loginURL, payload)
    #print(response.json()['token'])
    #yield response.json()['token']


def test_getUsers(get_token):
    token = get_token
    usersURL = baseURI + usersUrlPath
    headers = {'x-access-token': token}
    resp = getApiData(usersURL, headers)
    print(json.dumps(resp.json(), indent=4))
    assert resp.json()['users'][0]['email']
