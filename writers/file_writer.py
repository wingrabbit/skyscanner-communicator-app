from writers.base_writer import BaseWriter

class FileWriter(BaseWriter):

    def __init__(self, path) -> None:
        self.path = path

    def write(self, data):
        f = open("search_results/test.txt", 'a+')
        f.write(data)
        f.write('\n')
        f.close()