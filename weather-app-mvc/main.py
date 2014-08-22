
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
            url = "http://xml.weather.yahoo.com/forecastrss?p=" + zip
            #assemble the request
            request = urllib2.Request(url)
            #use the urllib2 to create an object to get the url
            opener = urllib2.build_opener()
            #use the url to get a result - request info from the API
            result = opener.open(request)

            #parse xml
            xmldoc = minidom.parse(result)

            self.response.write(xmldoc.getElementsByTagName('title')[0].firstChild.nodeValue)
            self.content = '<br/>'
            list = xmldoc.getElementsByTagName("yweather:forecast")
            for item in list:
                self.content += item.attributes['day'].value
                self.content += "   HIGH: " + item.attributes['high'].value
                self.content += "   LOW: " + item.attributes['low'].value
                self.content += "   HIGH: " + item.attributes['text'].value
                self.content += '<img src="images/' + item.attributes['code'].value + '.png" width="40" />'
                self.content += "<br/>"

            self.response.write(self.content)


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
