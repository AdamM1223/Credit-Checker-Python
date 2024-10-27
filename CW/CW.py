# CreditScore.py
''' 
A program that allows the user to work out their Credit Score by going through
the different criteria affecting said score, which is then returned in a professional style
once completed.
'''
# By Adam M


# Assigning the necessary variables to allow for them to be called into functions throughout the program

credit_score = 400 # base credit score
card = []   # empty list
electoral = ""      # the following 4 are for storing the answers given by the user
ccj = ""
account = ""
payments = ""
totalBal = 0.0
totalLim = 0.0
pound = u'\u00A3' # this is used for display purposes as visual studio will not accept the symbol for pound
creditCards = 0


def main(): # Defining the main function 
    global credit_score, card, creditCards  # This calls some global variables to be used within the main function

    # Main function calls on other functions that have been defined below, passing parameters to some of them

    cards() # Calls cards function
    cardInfo(creditCards) # Calls cardInfo function, passing in creditCards variable
    sumTotal()  # Calls sumTotal function
    totals(totalBal, totalLim)  # Calls totals function with 2 passed parameters
    newacc()    # Calls the newacc function 
    elect()     # Calls the elect function with 1 passed parameter
    missingPayment()    # Calls the missingPayment function with 1 passed parameter
    ccjcheck()  # Calls the ccjcheck function with 1 passed parameter
    display()   # Calls the display function with 1 passed parameter



def cards(): # define function cards 
    global creditCards # calls global variable creditCards


    while True:     # While loop begins to prompt the user for number of credit cards and stores as a variable
        try:        # try allows the code to take an input and then compares this to the below if statement, to determine what to do with the input
            creditCards = int(input("How many credit cards (0-3)? "))
            if not 0<= creditCards <= 3:    # If statement checks if input is not between 0 and 3, 
                raise ValueError            # if true, this returns a value error
        except ValueError:      # When a value error is returned, prompt the user to re-enter a valid number, this continues until one is given
            print("ERROR: Invalid number of cards - please re-enter: ")
        else:
            break   # When a valid input is given the while loop will break

    return creditCards      # returns creditCards variable for future use



def cardInfo(NoOfCards):  # define function cardInfo with 1 passed parameter (No)

    global card   # calls global variable for use
    Limit = False    # creates variables for use within function
    creditBalance = 0.0
    creditLimit = 0.0
    count = 0


    if 1 <= NoOfCards <= 3:    # If statement checks cards are within 1 and 3, so it can decide whether to run code within this statement
        while count < NoOfCards:    # If above is true, run a while loop that carries out for each card, we can do this by running this while a running count is less than the Number of Cards
               # creditBalance = input("What is the balance of card" + str(i + 1) + " (0-10,000)? ")
            Limit = False   # Set Limit to False for nested while loop to run once balance is retrieved

            try:    # try allows the code to take an input and then compares this to the below if statement, to determine what to do with the input
                creditBalance = float(input("What is the balance of card " + str(count +1) + " (" + pound + "0-10,000)? "))
                if not 0 <= creditBalance <= 10000: 
                    raise ValueError        # If input is not a valid input raise a value error for the program
            except ValueError:   # When a value error is returned, prompt the user to re-enter a valid number, this continues until one is given
                print("ERROR: Please enter a valid number. (0 - 10,000)")
            else:
                card.append(creditBalance)  # If valid input given, append the card list with the credit balance


                while Limit == False:   # while loop continues to retrieve credit limit
                    try:    # try allows the code to take an input and then compares this to the below if statement, to determine what to do with the input
                        creditLimit = float(input("What is the credit limit of card " + str(count+1) + " (" + pound + "0-10,000)? "))
                        if not 0 <= creditLimit <= 10000 or not creditLimit >= creditBalance:
                            raise ValueError     # If input is not a valid input raise a value error for the program
                    except ValueError:  # When a value error is returned, prompt the user to re-enter a valid number, this continues until one is given
                        print("ERROR: Please enter a valid number. (Larger than Balance, 0-10,000)")
                    else:
                        card.append(creditLimit) # If valid input given, appened the card list with the credit limit
                        count+= 1   # Increase count by 1 to ensure the first while loop runs the correct amount of times
                        Limit = True    # Set variable limit to true to break this nested while loop

    else:       # If cards is not between 1-3, this will return, as that means cards is equal to 0
        return  

    return card # If cards was between 1-3, this will return the card list



def newacc(): # define function newacc, which will retrieve the details of the new account question
    global credit_score, account    # calls global variables to be used within this function
    account = input("Have you made a new account in the past 6 months? Y/N ") # Prompts user for input to the question, stores as variable account
    account = account.upper()       # Ensures the answer is made uppercase
    while not account[0] == "Y" and not account[0] == "N":        # checks user input against conditions to decide if the code should continue
        account = input("Please only input Y or N, thank you: ")    # If the input is not valid, the user is prompted for a valid input until one is given
        account = account.upper()   # Ensures the answer is made uppercase 

    if account[0] == "Y":    # If elif statement to decide how the input will affect the user's credit score, with 2 different outcomes
        credit_score -= 30
        # print(str(credit_score)) # test line
        return credit_score
    elif account[0] == "N":
        credit_score += 50
        # print(str(credit_score)) # test line
        return credit_score, account    # return calculated credit_score and the input given for account



def elect():  # defines elect function, which will retrieve the details of the electoral question
    global electoral, credit_score    # calls global variables
    electoral = str(input("Have you enrolled onto the Electoral Roll? Y/N: "))   # Prompts user for an input to the question
    electoral = electoral.upper()       # This ensures the input is a capital letter
    while electoral[0] != "Y" and electoral[0] != "N":        # While loop to validate input
        electoral = input("Please enter either Y or N: ")   # While input is not valid, prompt user for a valid input
        electoral = electoral.upper()   # Ensures input is a capital
    if electoral[0] == "Y": # If else calculates the credit score calculation by determining if the first letter of the input was Y or not
        credit_score += 50
    else:
        credit_score -= 20

    # print("Credit Score so far is: " + str(credit_score)) # test line
    return credit_score, electoral    # returns calculated credit as well as the electoral input



def missingPayment():  # defines missing payment function, which will retrieve the details of the missing payments question
    global credit_score, payments   # calls global variables
    payments = str(input("Are there any records of missing payments? Y/N: "))   # Prompts user for an input
    payments = payments.upper()          # This ensures the input is a capital letter
    while payments[0] != "Y" and payments[0] != "N":  # while loop to check first letter of input against the conditions given
        payments = str(input("Please enter a valid response (Y/N): "))  # If first letter is not Y or N, prompts user for a valid response
        payments = payments.upper() # Capitalise input

    if payments[0] == "Y":  # If else calculates the credit score calculation by determining if the first letter of the input was Y or not
        credit_score -= 100
        # print('-100') # test line
    elif payments[0] == "N":    # If input was not Y, elif will run
        credit_score += 125
        # print('+125') # test line

    # print("Credit Score so far is: " + str(credit_score)) # test line
    return credit_score, payments  # return score and payments to program



def ccjcheck():     # defines missing payment function, which will retrieve the details of the CCJ question
    global ccj, credit_score      # calls global variables
    ccj = input("Do you have any CCJs? Y/N: ")  # Prompts user for an input
    ccj = ccj.upper()                   # Capitalise input
    while ccj[0] != "Y" and ccj[0] != "N":      # while loop to determine if the input was valid
        ccj = input("Please enter Y or N: ")    # if not valid, while loop will continue to prompt user for valid input
        ccj = ccj.upper()           # Capitalise input

    if ccj[0] == "Y":       # If else calculates the credit score calculation by determining if the first letter of the input was Y or not
        credit_score -= 150
        # print(str(credit_score))  # test line
    elif ccj[0] == "N":
        credit_score += 175
        # print(str(credit_score))  # test line

    # print("Credit Score so far is: " + str(credit_score)) # test line
    return credit_score, ccj   



def sumTotal():     # define sumTotal function which will calculate the total balance and the total limit by iterating through the list card
    global card, totalBal, totalLim     # calls global variables

    for i in range(len(card)):  # for loop that runs once for the length of the list cards
        if i == 0 or i % 2 == 0:    # if elif statement to check is the index of the value is even, if so then add this ontto the total Balance variable
            totalBal += card[i]
            # print(totalBal)   #test line

        elif i == 1 or i% 2 != 0:   # elif the index is odd, add this onto the total Limit variable 
            totalLim += card[i]
            # print(totalLim) # test line


    return totalBal, totalLim   # return values for total Balance and total Limit



def creditRating(credit_score):    # define creditRating function which takes the credit score as a parameter and passes the result this to our display function

    rating = "" # declares rating as an empty string variable

    if credit_score >= 800:         # if elif statement which determines which category the credit score has met, working from the top down
        rating = "EXCELLENT"
    elif 800 > credit_score >= 600:
        rating = "GOOD"
    elif 600 > credit_score >= 400:
        rating = "FAIR"
    elif 400 > credit_score >= 200:
        rating = "POOR"
    elif 200 > credit_score >= 0:
        rating = "VERY POOR"

    return rating       # Whichever rating was achieved is returned, which is used in our display function



def totals(total1, total2): # define totals function which is used for the calculations with our credit cards values, which affects the users credit score
    global card, credit_score, creditCards  # call global variables


    if total2 >= 5000:      # if elif to determine if the credit score will be positively or negatively affected by the second parameter (total Limit)
        credit_score+= 50
        # print("+50") #test line
       
    elif total2 <= 250:
        credit_score-= 20
        # print("-20") # test line
    
    if total1 <=50:     # if elif to determine if the credit score will be positively or negatively affected by the first parameter (total Balance)
        credit_score+= 60
        # print("+60") # test line
    elif total1 >= 15000:
        credit_score-= 30
        # print("-30") # test line

    if creditCards > 0:            # if statement to check if number of credit cards is bigger than 0, if so then the nested if will run
        if total1 <= (total2/10*3):         # if elif to determine if the credit score will be affected using calculations
            credit_score+= 90               # if balance is below 30% or above 90% the score will be affected
            # print("+90") # test line
        elif total1 >= (total2/10*9):
            credit_score-= 50
            # print("-50") # test line

    return credit_score     # returns credit score 



def DecimalPlaces(value):       # define decimal places function, which takes one parameter, this is used to quickly format values to 2 decimal places
     value = "{:.2f}".format(value)     # creates a variable which is the inputted parameter formatted to 2 decimal places
     return value           # return value to wherever the function is called



def dash(times):    # define dash function which allows us to decide how many times we would like to print '=' on our display function
    print("=" * times)  # this will output '=' however many times is passed into the function



def yesOrNo(input):     # define yesOrNo function which retrieves the lengthened answer, which will be displayed in our display function
    if input[0] == "Y":     # if the first letter of our passed input is a Y, this will return a Yes
        response = "Yes"
        return response
    elif input[0] == "N":   # elif the first letter of our passed input is an N, this will return a No
        response = "No"
        return response



def display():     # defines the display function which is going to output all of the collected information and return the results of credit score
    global card, creditCards, credit_score, electoral, ccj, account, totalBal, totalLim  # calls global variables to be used within this function
    cards = int(len(card) / 2)  # creates variable which finds the length of the list and divides by 2 to determine how many cards there were

    count = 0       # creates count variable and sets to keep track of the current card number
    print("Summary")        # Output information to the user
    dash(7)             # calls dash function and outputs this 7 times for professional look
    print("Number of credit cards: " + "{:.0f}".format(creditCards))        # Outputs the number of cards
    print("\n" + "Card\t Balance\t Limit")      
    dash(30)        # calls dash function and outputs this 30 times for professional look
    i = 0
    while i in range(creditCards+(creditCards - 1)):        # while loop which ensures that the values of each card are displayed correctly
            print(str(count+1), "\t", pound + DecimalPlaces(card[i]), " \t", pound + DecimalPlaces(card[i+1]))  #   Decimal Places function formats the values to 2 decimal places and outputs to the user
            count += 1  # add one to count which keeps track of card number
            i += 2  # add 2 to i which will skip forward to the next card in the list, as each card has 2 values
    dash(30)        # calls dash function and outputs this 30 times for a professional look
    print("Total" + "\t" + pound + DecimalPlaces(totalBal) + "\t" + pound + DecimalPlaces(totalLim)) # Decimal Places function formats these values to 2 decimal places and outputs to the user

    print("New account in last 6 months?: \t  " + yesOrNo(account)) # Outputs account answer, with the returned value from yesOrNo function 
    print("Electoral roll?: \t\t  " + yesOrNo(electoral))   # Outputs electoral answer, with the returned value from yesOrNo function
    print("Missing Payments?: \t\t  " + yesOrNo(payments))  # Outputs payments answer, with the returned value from yesOrNo function
    print("CCJ?: \t\t\t\t  " + yesOrNo(ccj))    # Outputs ccj answer, with the returned value from yesOrNo function

    print("Credit Score Rating")   
    dash(19)        # Dash function will output 19 times for a professional look
    print("Score: \t" + str(credit_score))  # Outputs credit score to the user
    print("Indicator: " + creditRating(credit_score))   # Returns grade of the credit score by using the creditRating function


main() # Calls the main function

