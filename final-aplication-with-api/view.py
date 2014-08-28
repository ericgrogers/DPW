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

    def update_list(self):
        """Method to update the movie list"""
        for do in self.__mdo:  # loop through the do (data object) in the mdo (movie data objects) array
            self.__list_content += '''
<ul class="movie-titles">
    <li><a href="?i=''' + do.id + '">' + do.title + '''</a></li>
    <li>''' + do.year + '''</li>
</ul>'''  # create the html to display the movie list item and append the movie's id to the link created.

    # Getters and Setters for the MovieView() class

    @property  # property decorator
    def mdo(self):  # getter for the mdo array
        return self.__mdo  # return the private mdo array

    @mdo.setter  # setter decorator
    def mdo(self, o):  # setter for the mdo array
        self.__mdo = o  # set the private mdo array to the new value
        self.update_list()  # call the update list method

    @property  # property decorator
    def list_content(self):  # getter for the list_content
        return self.__list_content  # return the private list_content

    @property  # property decorator
    def movie_content(self):  # getter for the movie_content
        return self.__movie_content  # return the private movie_content

    @property  # property decorator
    def md(self):  # getter for the md (movie data)
        return self.__md  # return the private md (movie data)

    @md.setter  # setter decorator
    def md(self, new_md):  # setter for the md (movie data)
        self.__md = new_md  # set the private md to the new value
        self.update_movie()  # call the update_movie method


#######--- ABSTRACT CLASS ---#########
class PageView(object):
    """ABSTRACT PAGE CLASS TO BE USED AS A TEMPLATE FOR THE PAGES."""
    def __init__(self):  # initialize the PageView
        #setting boilerplate html for the head of the page
        self._head = '''
<!DOCTYPE html>
<html lang="en">
    <head>
      <meta charset="UTF-8">
       <title>Movie Buff</title>
       <link href='http://fonts.googleapis.com/css?family=Candal' rel='stylesheet' type='text/css'>
       <link type="text/css" rel="stylesheet" href="css/styles.css">
    </head>
    <body>'''
        #var to hold static body content
        self._body = '''
<h1>Movie Ndex</h1>'''
        # var to hold the page content
        self._content = ''
        #var to hold the closing tags at the page foot.
        self._close = '''
    </body>
</html>'''

    def compile_view(self):
        """Method for compiling the page view"""
        html = self._head + self._body + self._close  # concatenate the different html parts into a single variable, "html".
        return html  # return the html