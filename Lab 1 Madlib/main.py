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

     #if their response is less than 10, add 10 to it.
    if response < 10:
        print "That's not enough, I'm going to add some to it."
        response += 10

    #otherwise, if their response is greater than 100, subtract 20 from it.
    elif response > 100:
        print "That's too much, I'm going to subtract a little."
        response -= 20

    #otherwise, continue on.
    else:
        pass

    #return the value of their response.
    return response

'''Function to get the objects for the mad lib.'''
def object_question():

    #ask the user for an object name.
    response = raw_input("Please enter the name of an object. ")

    #if the response is not blank, return the value.
    if response != '':
        pass

    #otherwise, prompt the user again.
    else:
        print "I'm sorry, you cannot leave it blank. Please enter the name of an object."

    #return the value of their response.
    return response

'''Function to get the verbs for the mad lib.'''
def verb_question():

    #ask the user to enter a verb and save their response.
    response = raw_input("Please enter a verb (e.g. running, swimming etc.) ")

    #if their response is not empty, return the value of their response.
    if response != '':
        pass

    #otherwise, prompt them again.
    else:
        print "I'm sorry, you cannot leave it blank. Please enter a verb."

    #return the value of their response.
    return response

'''Function to gather all of the user's answers/responses.'''
def get_answers():

    #call the function for names 3 times and append the responses to the answers array.
    for i in range(0, 3):
        response = name_question()
        answers.append(response)

    #call the function for numbers 3 times and append the responses to the answers array.
    for i in range(0, 3):
        response = number_question()
        answers.append(response)

        #call the function for objects 3 times and append the responses to the answers array.
    for i in range(0, 3):
        response = object_question()
        answers.append(response)

    #call the function for verbs 2 times and append the responses to the answers array.
    for i in range(0, 2):
        response = verb_question()
        answers.append(response)
