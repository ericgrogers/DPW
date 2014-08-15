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

        p = Page()

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

        #populate the package details using the package location within the pkgs array.
        def build_package(index):

            #shortcut for the index (package location within the array)
            i = index

            #populate the package attributes with the correct information using the index.
            p.package_name = pkgs[i].package_name
            p.expires = pkgs[i].expires
            p.hours = pkgs[i].hours

            #converting the rate into a string to be able to concatenate the dollar sign in front of the value.
            p.rate = '$' + str(pkgs[i].rate)
            p.discount_rate = str(pkgs[i].discount_rate) + '%'
            p.total = '$' + str(pkgs[i].total)
            p.discounted_total = '$' + str(pkgs[i].discounted_total)

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

        #bronze package object
        bronze = MaintenancePackage()
        bronze.package_name = "Bronze"
        bronze.expires = "2 weeks from start."
        bronze.hours = 24
        bronze.rate = 60
        bronze.discount = 0.1
        bronze.discount_rate = 10
        bronze.total = get_total(bronze)
        bronze.discounted_total = get_discounted_total(bronze)

        #silver package object
        silver = MaintenancePackage()
        silver.package_name = "Silver"
        silver.expires = "1 month from start."
        silver.hours = 40
        silver.rate = 60
        silver.discount = 0.1
        silver.discount_rate = 10
        silver.total = get_total(silver)
        silver.discounted_total = get_discounted_total(silver)

        #gold package object
        gold = MaintenancePackage()
        gold.package_name = "Gold"
        gold.expires = "3 months from start."
        gold.hours = 120
        gold.rate = 50
        gold.discount = 0.2
        gold.discount_rate = 20
        gold.total = get_total(gold)
        gold.discounted_total = get_discounted_total(gold)

        #platinum package object
        platinum = MaintenancePackage()
        platinum.package_name = "Platinum"
        platinum.expires = "6 months from start."
        platinum.hours = 240
        platinum.rate = 50
        platinum.discount = 0.2
        platinum.discount_rate = 20
        platinum.total = get_total(platinum)
        platinum.discounted_total = get_discounted_total(platinum)

        #create an array of the packages
        pkgs = [basic, bronze, silver, gold, platinum]

        #if a GET request is made.
        if self.request.GET:

            #call the show labels method from the Page() class.
            p.show_labels()

            #call the select_package() function
            select_package()
        #compile the page html and write it to the document.
        self.response.write(p.compiler())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
