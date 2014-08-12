
import webapp2
from pages import Page #import the Page class from the pages package.

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.body = "Miss Piggy likes Kermit De Frog"

        self.response.write(p.whole_page)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
