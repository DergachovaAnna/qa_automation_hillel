from lesson_16.txt_reader import TxtReader
from lesson_16.txt_writer import TxtWriter


class TxtProxyReaderWriter:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    @property
    def get_result(self):
        if self.__result == '':
            return f'No cache'
        else:
            return f'DATA IN CACHED FILE: \n {self.__result} \n'

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result

    def write_file(self, new_data, mode='w'):
        if mode == 'a':
            new_data = ',\n' + new_data
        self.__txt_writer.write(new_data, mode)
        self.__is_actual = False
        self.__result = ''
        return f'File updated'


if __name__ == '__main__':
    proxy_reader = TxtProxyReaderWriter('file.txt')

    print(proxy_reader.read_file())
    print(proxy_reader.get_result)
    print('\n')
    print(proxy_reader.write_file('new1', 'a'))
    print(proxy_reader.get_result)
    print(proxy_reader.write_file('new2', 'a'))
    print(proxy_reader.read_file())
    print(proxy_reader.get_result)
    print(proxy_reader.write_file('new3', 'w'))
    print(proxy_reader.read_file())
    print(proxy_reader.get_result)
