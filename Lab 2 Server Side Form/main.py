"""
Eric Rogers
08/12/2014
Design Patterns for Web Programming
Simple Form
"""

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        

#Create a Page class to hold all of the view model templates.
class Page(object):
    def __init__(self):

        #set the default title
        self.title = "Eric Rogers | Contact"

        #set the location of the CSS file.
        self.css = "css/styles.css"

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
