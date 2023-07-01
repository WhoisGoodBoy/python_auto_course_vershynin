import psycopg2


class UserRepository:
    def __init__(self):
        self.connection = psycopg2.connect(
            user='postgres',
            password='d2z76ctb',
            host='localhost',
            port='5432',
            database='postgres'
        )
        self.__cursor = self.connection.cursor()

    def get_all(self):
        self.__cursor.execute(
            'SELECT * from users'
        )
        return self.__cursor.fetchall()

    def get_emails(self):
        self.__cursor.execute('select email from users;')
        return self.__cursor.fetchall()

    def update_one_first_name_by_email(self, email, name):
        self.__cursor.execute(
            f"update users set first_name = '{name}' where users.email = '{email}'"
        )

    def __del__(self):
        if self.connection:
            self.__cursor.close()
            self.connection.close()

user_repository = UserRepository()
print(user_repository.get_all())
print(user_repository.get_emails())
user_repository.update_one_first_name_by_email('a@a.a','Leonardo')
user_repository.connection.commit()
print(user_repository.get_all())