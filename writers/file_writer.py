from writers.base_writer import BaseWriter
from config import result_files_path

class FileWriter(BaseWriter):

    def __init__(self, path) -> None:
        self.path = f"{result_files_path}{path}.txt"
    
    def write_list(self, data):
        f = open(self.path, 'a+')
        for i in data:
            f.write(str(i))
            f.write('\n')
        f.close()
    
    def write_line(self, data):
        f = open(self.path, 'a+')
        f.write(str(data))
        f.write('\n')
        f.close()
        