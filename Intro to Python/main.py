#one line comments
'''
Doc Strings
'''

first_name = "Kermit"
last_name = "de Frog"

response = raw_input("Enter your name:  ")
if response != '':
    print response
else:
    print "nothing typed"


birth_year = 1975
current_year = 2014
age = current_year - birth_year
#print age

print "your are " + str(age) + " years old."

budget = 90

#conditional statements
if budget > 100:
    brand = "Nike"
    print "we can afford " + brand + " shoes."
elif budget > 70:
    print "we can at least get some generics."
else:
    #to simply skip on
    pass

#arrays
characters = ["leia", "luke", "chewy"]

#add to the array
characters.append("obi won")

#dictionary, somewhat like an object in JS
movies = dict()#create dictionary object
movies ={"Star Wars": "Darth Vader", "Silence of the Lambs": "Hannibal Lector"}
print movies["Star Wars"], movies["Silence of the Lambs"]


#loops

#while loop
i = 0
while i < 9:
    print "the count is ", i
    i += 1

# for loop
for i in range(0,10):
    print "The for count is ", i
    i+= 1

# for each
rappers = ['Tupac', 'Nelly', 'Sir-Mix-Alot']

for r in rappers:
    print "One of the best rappers is ", r


#functions----------------------

def calc_area(h,w):
    area = h * w
    return area
calc_area(20,40)


# using variables in strings
weight = 200
height = 63
message = ''' Your height is {height} and your weight is{weight}'''

message = message.format(**locals())

print message


#html example
title = "Contact Us"
body = "You can contact us @ example.com"

message = '''<!DOCTYPE html>
    <html lang='en'>
    <head>
    <title>{title}</title>
    </head>
    <body>
    {body}
    </body>
    </html>
    '''

message = message.format(**locals())

print message
