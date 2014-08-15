"""
Eric Rogers
08/14/2014
Design Patterns for Web Programming
Encapsulated Calculator
"""


#class for all of the page html markup
class Page(object):
    def __init__(self):

        #set the default page attributes
        self.title = 'Pricing'
        self.css = 'css/styles.css'
        self.package_name = 'Click on a button to view package details.'
        self.__expires = ''
        self.__hours = ''
        self.__rate = ''
        self.__discount_rate = ''
        self.__total = ''
        self.__discounted_total = ''
        self.expires_label = ''
        self.hours_label = ''
        self.rate_label = ''
        self.discount_rate_label = ''
        self.total_label = ''
        self.discounted_total_label = ''

              #page head section
        self.head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{self.title}</title>
    <link rel="stylesheet" type="text/css" href={self.css}>
</head>'''
        self.body = ''''''

        
         #page closing tags
        self.close = '''
</body>
</html>'''