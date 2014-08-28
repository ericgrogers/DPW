"""
Eric Rogers
08/25/14
Design Patterns for Web Programming
Final Project: Application with API
API: http://www.omdbapi.com/
"""


class MovieView(object):
    """This class handles how the data is displayed."""
    def __init__(self):  # initialize the MovieView
        self.__movie_content = ''  # movie content
        self.__md = ''  # movie data
        self.__mdo = []  # movie data objects array
        self.__list_content = ''  # movie list content