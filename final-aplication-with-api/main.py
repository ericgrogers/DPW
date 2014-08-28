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

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
