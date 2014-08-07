'''
Eric Rogers
08/06/14
Design Patterns for Web Programming
Assignment: Mad Lib
'''

'''Jack and Jill Mad Lib '''

#initialize an array to store the user's responses.
answers = []



'''Function to get the names for the mad lib.'''
def name_question():

    # Ask the user for a name and save their response.
    response = raw_input("Please enter a person's name. ")

    #if their response is not blank, return the response.
    if response != '':
        pass

    #otherwise, ask them again.
    else:
        print "I'm sorry, you cannot leave it blank. Please enter a person's name."
        name_question()

    #return their response.
    return response

'''Function to get the numbers for the mad lib.'''
def number_question():

    #instantiate the response
    response = 0

    #if the user enters anything other than a number, continue to ask for a number.
    while True:

        #try to parse the user input as an integer, if it passes, go to the next if statement.
        try:
            response = int(raw_input("Please enter a number. "))
            break

        #if an error is thrown, alert the user to use whole numbers and ask again.
        except ValueError:
            print "Please, only use whole numbers."
            number_question()