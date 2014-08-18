"""
Eric Rogers
08/17/14
Design Patterns for Web Programming
Final: Proof of Concept
"""

import webapp2
import urllib2
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        self.response.write(p.compile_view())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE html>
<html lang="en">
    <head>
      <meta charset="UTF-8">
       <title></title>
    </head>
    <body>'''

        self._body = ''
        self._close = '''
    </body>
</html>'''

    def compile_view(self):
        return self._head + self._body + self._close


class PageForm(Page):
    def __init__(self):
        super(PageForm, self).__init__()

        self._form_start = '<form method="GET">'
        self._form_end = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]

            try:
                self._form_inputs += '<input type="' + item[2] + '">'
            except:
                self._form_inputs += '" >'

    def compile_view(self):
        return self._head + self._body + self._form_start + self._form_inputs + self._form_end + self._close