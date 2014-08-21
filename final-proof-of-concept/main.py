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
        #creating instances of PageForm and ResultList
        p = PageForm()
        rl = ResultList()

        #input format is 'type', 'name/value', 'placeholder'
        p.inputs = [['text', 'search', 'Search by Title'], ['submit', 'Search']]

        #compile the initial page view
        self.response.write(p.compile_view())

        #if GET is called (submit search)
        if self.request.GET:

            #set the search var in ResultList to the value of the search input.
            rl.search = self.request.GET['search']
            #try compiling the view using the Result List method
            try:
                self.response.write(rl.compile_view())
            #if an error is thrown, the search was unsuccessful.
            except:
                p.body = "<h2>I'm sorry, I couldn't find what you are looking for. Please Try Again.</h2>"
                self.response.write(p.body)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


#Page Class
class Page(object):
    def __init__(self):

        #setting boilerplate html for the head of the page
        self._head = '''
<!DOCTYPE html>
<html lang="en">
    <head>
      <meta charset="UTF-8">
       <title>Movie Buff</title>
       <link type="text/css" rel="stylesheet" href="css/styles.css">
    </head>
    <body>'''

        #var to hold the body content
        self._body = '''
<h1>Movie Buff</h1>'''

        #var to hold the closing tags at the page foot.
        self._close = '''
    </body>
</html>'''

    #method to compile the page view.
    def compile_view(self):
        html = self._head + self._body + self._close
        return html

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, new_value):
        self._body = new_value


#class for the page form
class PageForm(Page):
    def __init__(self):
        #inherits from the Page() class
        super(PageForm, self).__init__()

        #defining the form attributes.
        self._form_start = '<form method="GET">'
        self._form_end = '</form>'
        self.__inputs = []
        self._form_inputs = ''

    #getter for the inputs array.
    @property
    def inputs(self):
        return self._form_inputs

    #setter for the inputs array.
    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr
        #cyle through the array and create the form inputs.
        for item in arr:
            #try to create this style of input.
            try:
                self._form_inputs += '<input type="' + item[0] + '" name="' + item[1] + '" placeholder="' + item[2] + '">'
            #otherwise, use this style of input.
            except:
                self._form_inputs += '<input type="' + item[0] + '" value="' + item[1] + '">'

    #method to compile the page view (overrides compile_view in the Page() class.)
    def compile_view(self):
        return self._head + self._body + self._form_start + self._form_inputs + self._form_end + self._close


class ResultList(PageForm):
    def __init__(self):
        super(ResultList, self).__init__()
        self.search = ''
        self._title = ''
        self._year = ''
        self._rated = ''
        self._released = ''
        self._runtime = ''
        self._genre = ''
        self._director = ''
        self._writer = ''
        self._actors = ''
        self._plot = ''
        self._lang = ''
        self._country = ''
        self._awards = ''
        self._poster = ''
        self.__result_start = '''
    <div id="results">
        <ul>'''
        self.__result_body = ''
        self.__result_end = '''
    </div>'''

    def compile_view(self):
        url = "http://www.omdbapi.com/?plot=full&t=" + self.search
        url = url.replace(' ', '%20')
        request = urllib2.Request(url)
        opener = urllib2.build_opener()
        result = opener.open(request)
        jdoc = json.load(result)

        self._title = jdoc['Title']
        self._year = jdoc['Year']
        self._rated = jdoc['Rated']
        self._released = jdoc['Released']
        self._runtime = jdoc['Runtime']
        self._genre = jdoc['Genre']
        self._director = jdoc['Director']
        self._writer = jdoc['Writer']
        self._actors = jdoc['Actors']
        self._plot = jdoc['Plot']
        self._lang = jdoc['Language']
        self._country = jdoc['Country']
        self._awards = jdoc['Awards']
        self._poster = jdoc['Poster']

        self.__result_body = '''
    <li>Title: {self._title}</li>
    <li>Year: {self._year}</li>
    <li>Rated: {self._rated}</li>
    <li>Released: {self._released}</li>
    <li>Run Time: {self._runtime}</li>
    <li>Genre: {self._genre}</li>
    <li>Director: {self._director}</li>
    <li>Writer: {self._writer}</li>
    <li>Actors: {self._actors}</li>
    <li>Plot: {self._plot}</li>
    <li>Languages: {self._lang}</li>
    <li>Country: {self._country}</li>
    <li>Awards: {self._awards}</li>
</ul>
<p><img src={self._poster} alt="" /></p>'''

        self.__result_body = self.__result_body.format(**locals())

        return self.__result_start + self.__result_body + self.__result_end