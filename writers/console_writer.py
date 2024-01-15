from writers.base_writer import BaseWriter

class ConsoleWriter(BaseWriter):
    def write(self, data):
        print(data)