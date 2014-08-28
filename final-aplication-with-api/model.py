"""
Eric Rogers
08/25/14
Design Patterns for Web Programming
Final Project: Application with API
API: http://www.omdbapi.com/
"""

# import the necessary libraries
import urllib2
import json


class MovieModel(object):
    """This model handles fetching, parsing, and sorting the data from the API."""

    def __init__(self):
        self.__url = "http://www.omdbapi.com/"  # setting the base url for the API
        self.__search = ''  # used to store search values
        self.__id = ''  # holds the movie id
        self.__jdoc = ''  # holds the returned json
