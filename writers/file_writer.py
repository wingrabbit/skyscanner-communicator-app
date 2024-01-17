from writers.base_writer import BaseWriter

class FileWriter(BaseWriter):

    def __init__(self, path) -> None:
        self.path = path
    
    def write_list(self, data):
        f = open("search_results/test.txt", 'a+')
        for i in data:
            f.write(str(i))
            f.write('\n')
        f.close()
    
    def write_line(self, data):
        f = open("search_results/test.txt", 'a+')
        f.write(str(data))
        f.write('\n')
        f.close()
        