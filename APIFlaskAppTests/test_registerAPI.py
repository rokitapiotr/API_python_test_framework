from utils.apiUtils import postApiData
from utils.fileUtils import getJsonFromFile
from utils.confparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
urlPath = '/register'
registerJsonFile = 'registerApiValid.json'


def test_register_API():
    url = baseURI + urlPath
    payload = getJsonFromFile(registerJsonFile)
    resp = postApiData(url, payload)
    assert resp.status_code == 201
