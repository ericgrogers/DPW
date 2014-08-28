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

    def get_title(self):
        """Method for handling a movie's data."""

        self.__url += "?plot=full&i="  # sets the url to a search by id, that returns a full length plot
        request = urllib2.Request(self.__url + self.__id)  # construct the request
        opener = urllib2.build_opener()  # create an object to get the url
        result = opener.open(request)  # use the url to request info from the API
        self.__jdoc = json.load(result)  # parse the JSON returned from the API
