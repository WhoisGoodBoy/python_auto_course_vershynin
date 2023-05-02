from abc import ABC, abstractmethod


class BeerFactory(ABC):
    _beer_type:str = ''

    @abstractmethod
    def get_beer(self, name:str):
        pass



class StoutFactory(BeerFactory):
    _beer_type = 'stout'

    def __init__(self):
        self.name = 'Guiness'
        self.__positions = ['Milk', 'Dry']

    @property
    def positions(self):
        return self.__positions

    def get_beer(self, name:str):
        if name == 'Milk':
            return 'here`s your milk stout'


class IPAFactory(BeerFactory):
    _beer_type = 'ipa'

    def __init__(self):
        self.name = 'varvar'
        self.__positions = ['Golden', 'American']

    @property
    def positions(self):
        return self.__positions

class AbstractBeerFactory:
    @staticmethod
    def get_factory(beer_type:str):
        if beer_type == 'stout':
            return StoutFactory()
        elif beer_type == 'ipa':
            return IPAFactory()

stout_factory =AbstractBeerFactory.get_factory('stout')
print(stout_factory.get_beer('Milk'))
print()