import requests
from lesson27.app import config


class PeopleService:
    def __init__(self):
        self.__people_url = f"{config['host']}people"

    def get_person(self, id):
        return requests.get(f"{self.__people_url}/{id}")

