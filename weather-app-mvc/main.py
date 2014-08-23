
import webapp2
import urllib2
from xml.dom import minidom


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['zip', 'text', 'Zip Code'], ['Submit', 'submit']]
        self.response.write(p.print_out())

        if self.request.GET:
            #get info from the API
            zip = self.request.GET['zip']
            wm = WeatherModel()
            wm.zip = self.request.GET['zip']
            wm.call_api()
            # self.response.write(xmldoc.getElementsByTagName('title')[0].firstChild.nodeValue)
            # self.content = '<br/>'
            # for item in list:
            #     self.content += item.attributes['day'].value
            #     self.content += "   HIGH: " + item.attributes['high'].value
            #     self.content += "   LOW: " + item.attributes['low'].value
            #     self.content += "   HIGH: " + item.attributes['text'].value
            #     self.content += '<img src="images/' + item.attributes['code'].value + '.png" width="40" />'
            #     self.content += "<br/>"
            #
            # self.response.write(self.content)


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
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
