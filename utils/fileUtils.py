import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
TEST_DATA_DIR = BASE_DIR.joinpath('test_data')


def getJsonFromFile(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        return json.load(file)


def getCsvDataAsDict(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        csvFile = csv.reader(file)
        headers = next(csvFile)
        dictList = [dict(zip(headers, row)) for row in csvFile]

    return dictList


def getDataAsList(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        lines = list(csvFile)
    return lines


def getDataAsTuple(filename):
    dataList = getDataAsList(filename)
    return [(lines[:2], lines[2]) for lines in dataList]
