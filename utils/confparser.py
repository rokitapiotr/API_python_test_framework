import configparser
from pathlib import Path


configFile = 'petsqa.ini'
configFileDirectory = 'config'
configFileFlaskApp = 'qa.ini'

config = configparser.ConfigParser()
configFlaskApp = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(configFileDirectory).joinpath(configFile)
CONFIG_FILE_FLASKAPP = BASE_DIR.joinpath(configFileDirectory).joinpath(configFileFlaskApp)

config.read(CONFIG_FILE)
configFlaskApp.read(CONFIG_FILE_FLASKAPP)


def getPetAPIurl():
    return config['pet']['url']


def getStoreAPIurl():
    return config['store']['url']


def getFlaskAppBaseURL():
    return (
        'http://'
        + configFlaskApp['flaskapp']['url']
        + ":"
        + configFlaskApp['flaskapp']['port']
        + '/api'
    )


print(getPetAPIurl())
print(getStoreAPIurl())
print(getFlaskAppBaseURL())