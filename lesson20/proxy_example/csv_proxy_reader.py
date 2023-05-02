from lesson20.proxy_example.reader import Reader
from lesson20.proxy_example.csv_reader import CSVReader


class CSVProxyReader(Reader):
    def __init__(self,csv_reader:CSVReader):
        self.__result = ""
        self.__is_actual = False
        self.__reader = csv_reader

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read()
            self.__is_actual = True
            return self.__result


    def update_actual_status(self, status:bool):
        self.__is_actual = status