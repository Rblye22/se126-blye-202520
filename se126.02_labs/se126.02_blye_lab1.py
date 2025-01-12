#Robert Blye
#SE126.02
#Lab1
#1-7-2025 [W1D2]

#PROGRAM PROMPT: 
#it is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.


#VARIABLE DICTIONARY:

#--------IMPORTS----------------------------------------------
from os import system, name
#--------FUNCTIONS--------------------------------------------

max_cap = 1
people = 1
response = 1

def clear():
    if name == 'nt': 
        _ = system('cls') 
    else:
         _ = system('clear')


def difference(people, max_cap):
    '''This is the function that tells the difference of people in the room and the max capacity.'''

    max_cap = (int(input("\n\tWhat is the maximun capacity for that room?")))
    people = (int(input("\n\tHow many people are attending this meeting?")))

    while answer =="y":  
    
        if people <= max_cap:
            open_seats = max_cap - people 

            print(f"\n\t{open_seats} people can be added to the meeting and still meet fire regulations.")

        if people >= max_cap:
            ppl_over = people - max_cap
            ppl_over + 1

            print(f"\n\t{ppl_over} people must be removed from the meeting to meet fire regulations.")

        return answer

def decision(response):
    '''This is the function to ask the user if they would like to continue to check the program for another meeting attendance information.'''
   
    #while loop trap - ensure user provides valid value before moving on
    
    response = input("\n\tWould you like to enter another meeting? [y/n]: ").lower()

    while response != "y" and response != "n":
        print("***INVALID ENTRY!***")
        response = input("\n\tWould you like to check another meeting? [y/n]: ").lower()

    return response
            


#--------MAIN EXECUTING CODE----------------------------------
clear()

answer = "y"


#start of loop - will be based on answer, and user can change value at end of loop
while answer == "y":
    print("\n\tWelcome to the Fire Department fire saftey program!")

    print(input("\n\tPlease enter your meeting name:"))

    difference(people,max_cap)

    response = decision(response)


