from lesson31.session import session
from lesson31.models.users import Users


class Users_Repository:
    def __init__(self):
        self.__session = session


    def get_one(self):
        print(self.__session.get(Users, {'id':'aaaaaaaa'}))

    def get_all(self):
        for user in self.__session.query(Users).all():
            print(user)

users_repository = Users_Repository()
users_repository.get_all()
users_repository.get_one()