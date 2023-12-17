import json

import requests


def getApiData(url, optionalHeader=None):
    headers = {'Content-Type': 'application/json'}
    if optionalHeader and isinstance(optionalHeader, dict):
        headers |= optionalHeader
    response = requests.get(url, headers=headers, verify=False)
    print(f"Request URL: {url}")
    print('Request Header:', response.request.headers)
    print('Response Header:', response.headers)
    print('Response Content:', response.text)
    return response


def postApiData(url, body):
    headers = {'Content-Type': 'application/json'}
    print(f"Request URL: {url}")
    print('Response Body:', json.dumps(body))
    return requests.post(url, headers=headers, verify=False, json=body)
