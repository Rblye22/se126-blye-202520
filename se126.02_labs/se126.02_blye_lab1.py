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
response = 0

def clear():
    if name == 'nt': 
        _ = system('cls') 
    else:
         _ = system('clear')


def difference(people, max_cap):
    '''This is the function that tells the difference of people in the room and the max capacity.'''
    while people <= max_cap:
        open_seats = max_cap - people 

        print(f"{open_seats} people can be added to the meeting and still meet fire regulations ")

        if people >= max_cap:

            ppl_over = people - max_cap
            ppl_over + 1
            print(f"{ppl_over} people must be removed from the meeting to meet fire regulations.")

            return answer

def decision(response):
    '''This is the function to ask the user if they would like to continue to check the program for another meeting attendance information."'''

    answer = input("\t\tWould you like to check another meeting? [y/n]: ").lower()
    
    while answer =="y" or answer =="n":
        if answer == "y":
            answer == "y"

        if answer == "n":
         answer != "y"

        elif answer != "y" or answer != "n":
            print("***INVALID ENTRY!***")
            answer = input("\t\tWould you like to check anothe meeting? [y/n]: ").lower()

            return answer
            


#--------MAIN EXECUTING CODE----------------------------------

clear()
answer = "y"

#start of loop - will be based on answer, and user can change value at end of loop
while answer == "y":
    print("\tWelcome to the Fire Department fire saftey program!")

    print(input("\tPlease enter your meeting name:"))

    print(int(input("\tHow many people are attending this meeting?")))

    print(int(input("\tWhat is the maximun capacity for that room?")))

    difference(people,max_cap)

    decision(response)

else:
    print("Thank you for your complaince with our fire code")