

class Bus:
    def __init__(self):
        self.message = None

    def read(self):
        return self.message

    def write(self, message):
        self.message = message