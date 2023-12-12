import requests


# Get API call and return response data
def getAPIData(url):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    assert len(data) > 0, 'Empty response!!!'
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken
