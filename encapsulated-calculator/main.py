"""
Eric Rogers
08/14/2014
Design Patterns for Web Programming
Encapsulated Calculator
"""


import webapp2
from pages import Page
from packages import MaintenancePackage


class MainHandler(webapp2.RequestHandler):
    def get(self):

        #basic package object
        basic = MaintenancePackage()
        basic.package_name = "Basic"
        basic.expires = "48 hours from start."
        basic.hours = 6
        basic.rate = 65
        basic.discount = 0.1
        basic.discount_rate = 10
        basic.total = get_total(basic)
        basic.discounted_total = get_discounted_total(basic)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
