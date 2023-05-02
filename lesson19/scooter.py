

def singleton(_class):
    def inner(*args):
        if not hasattr(_class, 'instance'):
            setattr(_class, 'instance', _class(*args))
        return  getattr(_class, 'instance')
    return inner


@singleton
class Scooter:
    def __init__(self,color:str, wheel_size:int):
        self.color = color
        self.__wheels = wheel_size


scooter1 = Scooter("Black", 20)
scooter2 = Scooter("white", 30)
scooter1.color = 'Blue'
print()
del scooter1
del scooter2
print()
scooter3 = Scooter("Red", 30)
print()
