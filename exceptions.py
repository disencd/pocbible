

class ErrorHandler(Exception):
    def __init__(self, input):
        self.input = input

    def __str__(self):
        return '{} match not found in Bible'.format(self.input.capitalize())
