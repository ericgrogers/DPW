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

        #method to calculate the total depending on which package was selected.
        def get_total(package):

            #multiply hours by rate to get the total
            total = package.hours * package.rate

            #return a formatted total, removing decimal places and adding a comma in the proper places.
            return "{:,.0f}".format(total)

        #function to calculate the discounted total
        def get_discounted_total(package):

            #hours multiplied by rate minus the discount, rounded with the int() method
            total = int(package.hours * package.rate - (package.hours * package.rate * package.discount))

            #return a formatted total, removing decimal places and adding a comma in the proper places.
            return "{:,.0f}".format(total)

        #select the appropriate package using GET when the user clicks on one of the links.
        def select_package():

            #set pack to the package name
            pack = self.request.GET['package']

            #check each package name for a match and call build_package() using the index location of the package within pkgs.
            if pack == 'basic':
                build_package(0)
            elif pack == 'bronze':
                build_package(1)
            elif pack == 'silver':
                build_package(2)
            elif pack == 'gold':
                build_package(3)
            elif pack == 'platinum':
                build_package(4)

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

        #create an array of the packages
        pkgs = [basic, bronze, silver, gold, platinum]

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
