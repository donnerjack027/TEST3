"""
Custom exception definitions
"""


class Error(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)

class ParseError(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)
