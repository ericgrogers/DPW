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
        #page body section
        self.body = '''
<body>
<header>
    <h1>Eric Rogers</h1>
    <h2>designer/developer</h2>
    <nav>
        <ul>
            <li><a class="active_link" href="#">pricing</a></li>
            <li><a href="#">portfolio</a></li>
            <li><a href="#">contact</a></li>
        </ul>
    </nav>
</header>

<article>
    <h3>Maintenance Packages</h3>
    <div id="packages">
        <ul class="pkg-nav">
            <li><a class="pkg-nav-active" href="?package=basic">Basic</a></li>
            <li><a href="?package=bronze">Bronze</a></li>
            <li><a href="?package=silver">Silver</a></li>
            <li><a href="?package=gold">Gold</a></li>
            <li><a href="?package=platinum">Platinum</a></li>
        </ul>
        <h3 class="pkg-name">{self.package_name}</h3>
        <table>
            <tr>
                <th>{self.expires_label}</th>
                <td>{self.expires}</td>
            </tr>
            <tr>
                <th>{self.hours_label}</th>
                <td>{self.hours}</td>
            </tr>
            <tr>
                <th>{self.rate_label}</th>
                <td>{self.rate}</td>
            </tr>
            <tr>
                <th>{self.discount_rate_label}</th>
                <td>{self.discount_rate}</td>
            </tr>
        </table>

        <ul class="totals">
            <li>{self.total_label}</li>
            <li>{self.total}</li>
            <li>{self.discounted_total_label}</li>
            <li>{self.discounted_total}</li>
        </ul>
    </div>

    <div id="info">
        <p>I provide a variety of services to clients as part of a maintenance package in order to ensure that the
            client's websites and applications continue to function as desired. I offer several different package options so that you don't have to pay for more than what you need. Maintenance packages will not automatically start upon purchase. You will be provided with a range of start dates to choose from after purchase.</p>
        <p>Even if you are not a current client, I can provide maintenance for your websites or applications.</p>
        <h4>Some of the services that I provide include:</h4>
        <ul>
            <li>Troubleshooting.</li>
            <li>New Functionality.</li>
            <li>Upgrading Components.</li>
            <li>New Pages or Sections.</li>
            <li>SEO Optimization.</li>
        </ul>
    </div>

    <h5>Discounted rate only applies to returning customers.</h5>
</article>'''

        #page closing tags
        self.close = '''
</body>
</html>'''

    #method to show the labels for each attribute by populating the values.
    def show_labels(self):
        self.expires_label = 'Expires After:'
        self.hours_label = "Hours Included:"
        self.rate_label = "Hourly Rate:"
        self.discount_rate_label = "Discount Rate:"
        self.total_label = "Total:"
        self.discounted_total_label = "Discounted:"

    #getters and setters for the page attributes(properties)
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
