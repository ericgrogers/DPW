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

        # Sorting the Movie Data
        md = MovieData()  # create an instance of the MovieData object
        md.title = self.__jdoc['Title']  # set the movie's title
        md.year = self.__jdoc['Year']  # set the movie's year
        md.rated = self.__jdoc['Rated']  # set the movie's rating
        md.released = self.__jdoc['Released']  # set the movie's release date
        md.runtime = self.__jdoc['Runtime']  # set the movie's runtime
        md.genre = self.__jdoc['Genre']  # set the movie's genre