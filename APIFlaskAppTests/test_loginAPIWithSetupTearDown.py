import pytest
import random
from utils.apiUtils import postApiData, delApiData
from utils.fileUtils import getJsonFromFile
from utils.confparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
regUrlPath = '/register'
loginUrlPath = '/login'
delUrlPath = '/delete'
registerJsonFile = 'registerApiValid.json'
randomNum = random.randint(1, 5000)
print(randomNum)
eMail = f'automateUser@auto{randomNum}'
password = '1234'


@pytest.fixture()
def reg_user():
    payload = getJsonFromFile(registerJsonFile)
    regURL = baseURI + regUrlPath
    reg_response = postApiData(regURL, payload)
    print(f"Registration Response: {reg_response.text}")
    assert reg_response.status_code == 201
    assert reg_response.json()['id']
    yield reg_response.json()
    delUrl = baseURI + delUrlPath
    loginUrl = baseURI + loginUrlPath
    login_resp = postApiData(loginUrl, payload)
    token = login_resp.json()['token']
    headers = {'x-access-token': token}
    payload = {'id': reg_response.json()['id']}
    del_resp = delApiData(delUrl, payload, headers)
    assert del_resp.status_code == 200
    assert del_resp.json()['id'] == reg_response.json()['id']


def test_logicCorrectCreds(reg_user):
    payload = getPayloadDict_RegAPI(eMail, password)
    url = baseURI + loginUrlPath
    resp = postApiData(url, payload)
    assert resp.status_code == 200


def test_loginEmptyPassword(reg_user):
    data = reg_user
    payload = getPayloadDict_RegAPI(eMail, '')
    url = baseURI + loginUrlPath
    resp = postApiData(url, payload)
    assert resp.status_code == 401


def getPayloadDict_RegAPI(email=None, pwd=None):
    payload = getJsonFromFile(registerJsonFile)
    payload['email'] = email
    payload['password'] = pwd
    return payload
