"""
Eric Rogers
08/25/14
Design Patterns for Web Programming
Final Project: Application with API
API: http://www.omdbapi.com/
"""


class MovieView(object):
    """This class handles how the data is displayed."""
    def __init__(self):
        self.__movie_content = ''
        self.__md = ''
        self.__mdo = []
        self.__list_content = ''