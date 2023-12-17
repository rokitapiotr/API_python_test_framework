import pytest
from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.confparser import getFlaskAppBaseURL

loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
loginURLPath = '/login'


@pytest.fixture
def get_token():
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    response = postApiData(loginURL, payload)
    print(response.json()['token'])
    yield response.json()['token']
