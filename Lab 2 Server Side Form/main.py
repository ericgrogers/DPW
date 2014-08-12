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

         #create the head section of the page.
        self.head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{self.title}</title>
    <link rel="stylesheet" type="text/css" href={self.css}>
</head>
<body>
<header>
    <h1>Eric Rogers</h1>
    <h2>designer/developer</h2>
    <nav>
        <ul>
            <li><a href="#">pricing</a></li>
            <li><a href="#">portfolio</a></li>
            <li><a class="active_link" href="#">contact</a></li>
        </ul>
    </nav>
</header>'''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
