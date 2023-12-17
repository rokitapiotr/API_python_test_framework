from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.confparser import getFlaskAppBaseURL

loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
loginURLPath = '/login'
usersUrlPath = '/users'


def test_getUserDemo():
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    response = postApiData(loginURL, payload)
    print(response.json()['token'])
    token = response.json()['token']
    userURL = baseURI + usersUrlPath
    headers = {'x-access-token': token}
    resp = getApiData(userURL, headers)
    print(resp.json())
