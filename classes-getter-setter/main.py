
import webapp2
from pages import Page #import the Page class from the pages package.

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
