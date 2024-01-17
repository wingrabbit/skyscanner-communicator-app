from writers.base_writer import BaseWriter

class ConsoleWriter(BaseWriter):
    
    def write_line(self, data):
        print(data)

    def write_list(self, data):
        for i in data:
            print(data)