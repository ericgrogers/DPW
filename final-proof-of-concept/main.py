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
        p = PageForm()
        sr = SearchResult()

        #input format is 'type', 'name', 'placeholder', 'value'
        p.inputs = [['text', 'search', 'Search by Title'], ['submit', 'submit', 'Search', 'Search']]

        self.response.write(p.compile_view())

        if self.request.GET:

            sr.search = self.request.GET['search']

            try:
                self.response.write(sr.compile_view())
            except:
                self.response.write('<br /><p style="color: red">Please only enter a single word, without spaces.</p>')

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

        self._body = 'Enter a single word, no spaces.'
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
        return self._form_inputs

    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr
        for item in arr:
            try:
                self._form_inputs += '<input type="' + item[0] + '" name="' + item[1] + '" value="' + item[3]
            except:
                self._form_inputs += '<input type="' + item[0] + '" name="' + item[1]

            try:
                self._form_inputs += '" placeholder="' + item[2] + '">'
            except:
                self._form_inputs += '" >'

    def compile_view(self):
        return self._head + self._body + self._form_start + self._form_inputs + self._form_end + self._close


class SearchResult(PageForm):
    def __init__(self):
        super(SearchResult, self).__init__()
        self.search = ''
        self._title = ''
        self._year = ''
        self._type = ''
        self._t = ''
        self.__result_start = '''
    <div id="results">
        <ul>'''
        self.__result_body = ''
        self.__result_end = '''
        </ul>
    </div>'''

    def compile_view(self):
        url = "http://www.omdbapi.com/?s=" + self.search
        request = urllib2.Request(url)
        opener = urllib2.build_opener()
        result = opener.open(request)

        json_doc = json.load(result)

        for item in json_doc['Search']:
            self._t = item['Title']
            self._title = '<li><a href ="http://www.omdbapi.com/?t=' + self.t + '">Title: ' + item['Title'] + '</a></li>'
            self._year = '<li>Year: ' + item['Year'] + '</li>'
            self._type = '<li>Type: ' + item['Type'] + '</li>'
            self.__result_body += self._title + self._year + self._type + '<br />'

        return self.__result_start + self.__result_body + self.__result_end
