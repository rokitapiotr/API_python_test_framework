import configparser
from pathlib import Path


configFile = 'petsqa.ini'
configFileDirectory = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(configFileDirectory).joinpath(configFile)
config.read(CONFIG_FILE)


def getPetAPIurl():
    return config['pet']['url']


def getStoreAPIurl():
    return config['store']['url']


print(getPetAPIurl())
print(getStoreAPIurl())
