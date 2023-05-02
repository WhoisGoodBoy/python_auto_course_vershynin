from lesson20.proxy_example.reader import Reader


class CSVReader(Reader):
    def __init__(self, filename:str):
        self.__filename = filename

    def read(self):
        with open(self.__filename, 'r') as file:
            text = file.read()
        return text
