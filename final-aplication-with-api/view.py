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

    def update_movie(self):
        """Method to update the movie information displayed."""
        self.__movie_content = '''
<div id="results">
    <ul class="movie-info">'''  # set up the opening tags for the list
        self.__movie_content += '<li><span>Title: </span>' + self.__md[0] + '</li>'  # add the title from 'md' (movie data)
        self.__movie_content += '<li><span>Year: </span>' + self.__md[1] + '</li>'  # add the year from 'md' (movie data)
        self.__movie_content += '<li><span>Rated: </span>' + self.__md[2] + '</li>'  # add the rating from 'md' (movie data)
        self.__movie_content += '<li><span>Released: </span>' + self.__md[3] + '</li>'  # add the realease date from 'md' (movie data)
        self.__movie_content += '<li><span>Run Time: </span>' + self.__md[4] + '</li>'  # add the run time from 'md' (movie data)
        self.__movie_content += '<li><span>Genre: </span>' + self.__md[5] + '</li>'  # add the genre from 'md' (movie data)
        self.__movie_content += '<li><span>Director: </span>' + self.__md[6] + '</li>'  # add the director from 'md' (movie data)
        self.__movie_content += '<li><span>Writer: </span>' + self.__md[7] + '</li>'  # add the writer from 'md' (movie data)
        self.__movie_content += '<li><span>Actors: </span>' + self.__md[8] + '</li>'  # add the actor(s) from 'md' (movie data)
        self.__movie_content += '<li><span>Plot: </span>' + self.__md[9] + '</li>'  # add the plot from 'md' (movie data)
        self.__movie_content += '<li><span>Languages: </span>' + self.__md[10] + '</li>'  # add the language(s) from 'md' (movie data)
        self.__movie_content += '<li><span>Country: </span>' + self.__md[11] + '</li>'  # add the country from 'md' (movie data)
        self.__movie_content += '<li><span>Awards: </span>' + self.__md[12] + '</li>'  # add the award(s) from 'md' (movie data)
        self.__movie_content += '</ul>'  # close the unordered list
        self.__movie_content += '<p><img src="' + self.__md[13] + '" alt="" /></p></div>'  # add the poster from 'md' (movie data)