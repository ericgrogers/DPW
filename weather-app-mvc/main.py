
import webapp2
import urllib2
from xml.dom import minidom


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'Zip Code'], ['Submit', 'submit']]

        if self.request.GET:
            wm = WeatherModel()  # Creates the Model
            wm.zip = self.request.GET['zip']  # sends our Zip from the URL to the Model
            wm.call_api()  # Tells it to connect to the API

            wv = WeatherView()  # Creates the View
            wv.wdo = wm.dos  # takes objects from Model and gives them to View.
            p._body = wv.content
        self.response.write(p.print_out())


class WeatherView(object):
    """This class handles how the data is shown to the user."""
    def __init__(self):
        self.__wdo = []
        self.__content = '<br />'

    def update(self):
        for do in self.__wdo:
            self.__content += do.day
            self.__content += '<br /> High: ' + do.high + '<br />Low: ' + do.low
            self.__content += '<img src="images/' + do.code + '.png" width="50" />'
            self.__content += '<br /><br />'

    @property
    def content(self):
        return self.__content

    @property
    def wdo(self):
        pass

    @wdo.setter
    def wdo(self, arr):
        self.__wdo = arr
        self.update()

class WeatherModel(object):
    """ This model handles fetching, parsing, and sorting data from Yahoo! weather API"""
    def __init__(self):
        self.__url = "http://xml.weather.yahoo.com/forecastrss?p="
        self.__zip = ''
        self.__xmldoc = ''

    def call_api(self):
        # Requests and loads info from the API
        #assemble the request
        request = urllib2.Request(self.__url + self.__zip)
        #use the urllib2 to create an object to get the url
        opener = urllib2.build_opener()
        #use the url to get a result - request info from the API
        result = opener.open(request)
        #parse data
        self.__xmldoc = minidom.parse(result)


        # Sorting Data
        list = self.__xmldoc.getElementsByTagName("yweather:forecast")

        self._dos = []
        for tag in list:
            do = WeatherData()
            do.day = tag.attributes['day'].value
            do.high = tag.attributes['high'].value
            do.low = tag.attributes['low'].value
            do.date = tag.attributes['date'].value
            do.code = tag.attributes['code'].value
            self._dos.append(do)

    @property
    def dos(self):
        return self._dos


    @property
    def zip(self):
        pass

    @zip.setter
    def zip(self, z):
        self.__zip = z


class WeatherData(object):
    """ This Data Object holds the data fetched by the model and shown by the view."""
    def __init__(self):
        self.day = ''
        self.high = ''
        self.low = ''
        self.code = ''
        self.condition = ''
        self.date = ''


class Page(object):  # borrowing from the object class
    def __init__(self):
        self._head = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = 'Weather App'
        self._body_header = '<h1>Weather App using the Yahoo! Weather API</h1>'
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close


class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()

        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
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
                self._form_inputs += '" placeholder="' + item[2] + '">'

            except:
                self._form_inputs += '" >'

    def print_out(self):
        return self._head + self._body_header + self._form_open + self._form_inputs + self._body + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
