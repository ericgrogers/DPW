"""
Eric Rogers
08/14/2014
Design Patterns for Web Programming
Encapsulated Calculator
"""


#class for the maintenance packages.
class MaintenancePackage(object):
    def __init__(self):

        #making attributes private
        self.__package_name = ''
        self.__expires = ''
        self.__hours = 0
        self.__rate = 0
        self.__discount = 0.1
        self.__discount_rate = 0
        self.__total = 0
        self.__discounted_total = 0

    #getters and setters for each attribute(property)
    @property
    def package_name(self):
        return self.__package_name

    @package_name.setter
    def package_name(self, new_package_name):
        self.__package_name = new_package_name

    @property
    def expires(self):
        return self.__expires

    @expires.setter
    def expires(self, new_expires):
        self.__expires = new_expires

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, new_hours):
        self.__hours = new_hours

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, new_rate):
        self.__rate = new_rate

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, new_discount):
        self.__discount = new_discount

    @property
    def discount_rate(self):
        return self.__discount_rate

    @discount_rate.setter
    def discount_rate(self, new_discount_rate):
        self.__discount_rate = new_discount_rate

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, new_total):
        self.__total = new_total

    @property
    def discounted_total(self):
        return self.__discounted_total

    @discounted_total.setter
    def discounted_total(self, new_discounted_total):
        self.__discounted_total = new_discounted_total