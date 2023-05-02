class Human:
    def __init__(self, name:str, age:int, hair_color:str):
        self.__name = name
        self.__age = age
        self.__hair_color = hair_color

    def grow(self):
        self.__age += 1


    @property
    def age(self):
        return self.__age

    def change_hair_color(self, new_color:str):
        self.__hair_color = new_color

    @property
    def color(self):
        return self.__hair_color