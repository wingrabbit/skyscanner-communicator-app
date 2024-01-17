class BaseWriter:
    def write(self, data):
        if type(data) is list:
            self.write_list(data)
        else:
            self.write_line(data)

    def write_line(self, data):
        pass

    def write_list(self, data):
        pass