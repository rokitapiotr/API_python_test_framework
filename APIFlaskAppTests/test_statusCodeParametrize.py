import pytest
from utils.apiUtils import getApiData
from utils.confparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
urlPath = '/allusercount'

testData = [
    ('application/json', 200),
    ('application/xml', 406),
    ('multipart/mixed', 406),
    ('text/html', 200)
]


@pytest.mark.parametrize('types, status', testData)
def test_getAllUserCountStatus(types, status):
    url = baseURI + urlPath
    headers = {'Accept': types}
    resp = getApiData(url, headers)
    assert resp.status_code == status
