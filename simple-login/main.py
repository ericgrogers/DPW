
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):

        page_head = '''<!doctype html>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''

        page_body = '''<form method="GET">
            <label>Name:</label>
            <input type="text" name="name" />
            <label>Email:</label>
            <input type="text" name="email" />
            <input type="submit" value="Submit" />
        </form>
        '''
        page_close = '''
    </body>
<html>'''

        if self.request.GET:
            user = self.request.GET['name']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + email + ' ' + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
