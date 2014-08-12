"""
Eric Rogers
08/12/2014
Design Patterns for Web Programming
Simple Form
"""

import webapp2

from pages import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #create a shortcut to the Page() class
        p = Page()

        #if the GET method is invoked, grab the form values and set them to the proper keys
        if self.request.GET:

            #create a shortcut for self.request
            sr = self.request

            #set the page title.
            p.title = "Eric Rogers | Thank You!"

            #set the Page().name attribute to the input value submitted.
            p.name = sr.GET['name']

            #set the Page().telephone attribute to the input value submitted.
            p.telephone = sr.GET['telephone']

            #set the Page().email attribute to the input value submitted.
            p.email = sr.GET['email']

            #set the Page().interest attribute to the input value submitted.
            p.interest = sr.GET['interest']

            #set the Page().return_customer attribute to reflect the user's choice when checked.
            p.return_customer = 'Yes, please give me a 10% discount.'

            #try to grab the Page().return_customer checkbox value
            try:
                sr.GET['return_customer']

            #if there is no value, the server throws a KeyError meaning the box is not checked.
            except KeyError:

                #set the Page().return_customer attribute to reflect the user's choice when not checked.
                p.return_customer = 'No, I am a new customer.'

            #output Page().view2 to the page.
            self.response.write(p.view2())

        #otherwise, output Page().view1 to the page.
        else:
            self.response.write(p.view1())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
