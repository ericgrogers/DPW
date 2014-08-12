"""
Eric Rogers
08/12/2014
Design Patterns for Web Programming
Simple Form
"""

import webapp2


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


#Create a Page class to hold all of the view model templates.
class Page(object):
    def __init__(self):

        #set the default key values for the form inputs
        self.name = 'name'
        self.telephone = 'tele'
        self.email = 'email'
        self.interest = 'interest'
        self.return_customer = 'Yes, please give me a 10% discount.'

        #set the default title
        self.title = "Eric Rogers | Contact"

        #set the location of the CSS file.
        self.css = "css/styles.css"

         #create the head section of the page.
        self.head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{self.title}</title>
    <link rel="stylesheet" type="text/css" href={self.css}>
</head>
<body>
<header>
    <h1>Eric Rogers</h1>
    <h2>designer/developer</h2>
    <nav>
        <ul>
            <li><a href="#">pricing</a></li>
            <li><a href="#">portfolio</a></li>
            <li><a class="active_link" href="#">contact</a></li>
        </ul>
    </nav>
</header>'''

        #create the body section of the contact page (for view1)
        self.contact_body = '''
<form method="GET">
    <label for="name">Name</label>
    <input type="text" name="name" id="name" placeholder="John Doe" required="true">
    <label for="telephone">Telephone</label>
    <input type="tel" name="telephone" id="telephone" placeholder="555-555-5555" required="true">
    <label for="email">Email</label>
    <input type="email" name="email" id="email" placeholder="jdoe@example.com" required="true">
    <label for="interest">Interested in</label>
    <div id="select-box">
        <select name="interest" id="interest">
            <option>New Website</option>
            <option>Website Redesign</option>
            <option>Application Development</option>
        </select>
    </div>
    <input type="checkbox" name="return_customer" id="return_customer">
    <label for="return_customer"><span class="visible-checkbox"></span>I am a returning customer.</label>
    <input type="submit" value="Send">
</form>'''

        #create the body section for the thank you page (for view2)
        self.thanks_body = '''
<section>
    <h3>Thank You!</h3>
    <p>Hello {self.name},</p>
    <p>Thank you for contacting me about your project. I look forward to working with you!</p>
    <p>Here is a summary of the information that you submitted.</p>

    <dl>
        <dt>Name: </dt>
        <dd>{self.name}</dd>
        <dt>Telephone: </dt>
        <dd>{self.telephone}</dd>
        <dt>Email: </dt>
        <dd>{self.email}</dd>
        <dt>Interest: </dt>
        <dd>{self.interest}</dd>
        <dt>Return Customer: </dt>
        <dd>{self.return_customer}</dd>
    </dl>

    <p>I will be in contact with you soon so that we can discuss the details of your project.</p>
    <p>Sincerely,</p>
    <p>Eric Rogers</p>
</section>'''

        #create the closing section of the page.
        self.close = '''
</body>
</html>'''

    #create a function to compile and return view1 (contact page)
    def view1(self):

        #create a variable that contains the head, body, and close sections of the contact page.
        html = self.head + self.contact_body + self.close

        #format the page to allow variables in the HTML markup.
        html = html.format(**locals())

        #return the formatted contact page.
        return html

        #create a function to compile and return view2 (thank you page)
    def view2(self):

        #create a variable that contains the head, body, and close sections of the thank you page.
        html = self.head + self.thanks_body + self.close

        #format the page to allow variables in the HTML markup.
        html = html.format(**locals())

        #return the formatted thank you page.
        return html

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
