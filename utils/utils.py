import requests


# Get API call and return response data
def getAPIData(url):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    assert len(data) > 0, 'Empty response!!!'
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken


def putData(url, body):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, verify=False, json=body,  headers=headers)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken


def deleteData(url, optionalHeader=None):
    headers = {'Content-Type': 'application/json'}
    if optionalHeader and isinstance(optionalHeader, dict):
        headers |= optionalHeader

    response = requests.delete(url, verify=False, headers=headers)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken
