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

    def __init__(self):  # initialize the movie model
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
        md.director = self.__jdoc['Director']  # set the movie's director
        md.writer = self.__jdoc['Writer']  # set the movie's writer
        md.actors = self.__jdoc['Actors']  # set the movie's actor(s)
        md.plot = self.__jdoc['Plot']  # set the movie's plot
        md.lang = self.__jdoc['Language']  # set the movie's language(s)
        md.country = self.__jdoc['Country']  # set the movie's country
        md.awards = self.__jdoc['Awards']  # set the movie's award(s)
        md.poster = self.__jdoc['Poster']  # set the movie's poster
        md.id = self.__jdoc['imdbID']  # set the movie's id

        # Place the data into an array.
        self._title_data = [md.title, md.year, md.rated, md.released, md.runtime, md.genre, md.director, md.writer, md.actors, md.plot, md.lang, md.country, md.awards, md.poster, md.id]
        # When the API returns N/A for a data value, replace it with the text, 'Not enough data.'
        self._title_data = [value.replace('N/A', 'Not enough data.') for value in self._title_data]

    def get_list(self):
        """Method for getting the list of movies from a search."""
        self.__url += "?s="  # set the url to use the search function of the API
        self.__search = self.__search.replace(' ', '%20')  # replace spaces in the user search terms with the proper url encoding
        request = urllib2.Request(self.__url + self.__search)  # construct the request
        opener = urllib2.build_opener()  # create an object to get the url
        result = opener.open(request)  # use the url to request info from the API
        self.__jdoc = json.load(result)  # parse the JSON returned from the API


class MovieData(object):
    """This data object holds the Movie data fetched by the model and displayed by the view."""
    def __init__(self):  # initialize the movie data object
        self.title = ''  # movie title
        self.year = ''  # movie year
        self.rated = ''  # movie rating
        self.released = ''  # movie release date
        self.runtime = ''  # movie runtime
        self.genre = ''  # movie genre
        self.director = ''  # movie director
        self.writer = ''  # movie writer
        self.actors = ''  # movie actor(s)
        self.plot = ''  # movie plot
        self.lang = ''  # movie language(s)
        self.country = ''  # movie country
        self.awards = ''  # movie award(s)
        self.poster = ''  # movie poster
        self.imdb_ID = ''  # movie id


class MovieListData(object):
    """This object hold the data fetched from a user search"""
    def __init__(self):  # initialize the movie list data object
        self.title = ''  # set the movie title
        self.year = ''  # set the movie year
        self.id = ''  # set the movie id

