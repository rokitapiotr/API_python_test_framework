import pytest
from utils.apiUtils import postApiData
from utils.fileUtils import getCsvDataAsDict, getDataAsTuple
from utils.confparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
dataFile = 'registerApiData.csv'
urlPath = '/register'
dataFileWithStatus = 'registerApiDataWithStatus.csv'
getData = getDataAsTuple(dataFileWithStatus)


def test_dataDrivenRegApi():
    url = baseURI + urlPath
    print(url)
    payloadList = getCsvDataAsDict(dataFile)
    for datalines in payloadList:
        print(datalines)
        resp = postApiData(url, datalines)
        assert resp.status_code == 201
        data = resp.json()
        print(data)
        assert data['id']


@pytest.mark.parametrize("input, respStatus", getData)
def test_dataDrivenParametrized(input, respStatus):
    url = baseURI + urlPath
    keys = ['email', 'password']
    requestsDict = dict(zip(keys, input))
    print(requestsDict, respStatus)
    resp = postApiData(url, requestsDict)
    assert resp.status_code == int(respStatus)
