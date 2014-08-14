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