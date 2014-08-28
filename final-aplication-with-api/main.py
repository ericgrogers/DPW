"""
Eric Rogers
08/25/14
Design Patterns for Web Programming
Final Project: Application with API
API: http://www.omdbapi.com/
"""


import webapp2
from view import MovieView, PageFormView
from model import MovieModel


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = PageFormView()  # create an instance of PageFormView

        #input format is 'type', 'name/value', 'placeholder'
        p.inputs = [['text', 'search', 'Find a Movie'], ['submit', 'Search']]  # create the form inputs
        self.response.write(p.compile_view())  # compile the initial page load

        if self.request.GET:  # if the GET method is called
            if 'search' in self.request.GET:  # check the url for a 'search' parameter
                try:  # if search was found, try the following
                    mm = MovieModel()  # create an instance of MovieModel
                    mm.search = self.request.GET['search']  # set the MovieModel search attribute the the search value
                    mm.get_list()  # call the get_list method from MovieModel
                    mv = MovieView()  # create an instance of MovieView
                    mv.mdo = mm.dos  # set the MovieView mdo (movie data object) to the value of MovieModel dos (data objects)
                    self.response.write(mv.list_content)  # write the results of calling the MovieView list_content method
                except:  # otherwise
                    if not self.request.GET['search']:  # if a value for search is not found in the url
                        self.response.write(p.error1)  # tell the user they can't submit blanks
                    else:  # otherwise
                        self.response.write(p.error2)  # tell the user that their search was unsuccessful
            elif 'i' in self.request.GET:  # otherwise, if the parameter 'i' is found in the url
                try:  # try the following
                    mm = MovieModel()  # create an instance of MovieModel
                    mm.id = self.request.GET['i']  # set the MovieModel id to the value of the url parameter 'i'
                    mm.get_movie()  # call the MovieModel get_movie method
                    mv = MovieView()  # create an instance of MovieView
                    mv.md = mm.movie_data  # set the MovieView md (movie data) to the MovieModel movie_data
                    self.response.write(mv.movie_content)  # write the MovieView movie_content to the page
                except:  # otherwise
                    self.response.write(p.error2)  # tell the user that their search was unsuccessful
            else:  # otherwise
                self.response.write(p.error2)  # tell the user that their search was unsuccessful
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
