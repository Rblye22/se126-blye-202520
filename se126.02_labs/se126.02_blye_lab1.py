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

def clear():
    if name == 'nt': 
        _ = system('cls') 
    else:
         _ = system('clear')

people = int(input("Enter ammount of people attending the meeting."))
max_cap = int(input("Enter room max capacity"))

def difference(people, max_cap):
    '''This is the function that tells the difference of people in the room and the max capacity.'''
    people == int(input("Enter the amount of people attending the meeting"))
    max_cap == int(input("Enter the max capacity for the room"))
    while people <= max_cap:
        max_cap - people = answer + 1
        if people >= max_cap:
            people - max_cap = answer - 1

def decision(response):
    '''This is the response to the amount of peope who need to be removed or can be added to the meeting.'''
    while answer!="y" or answer !="Y":
        if people <= max_cap:
            print (f"You can add up to {answer} people")
            



#--------MAIN EXECUTING CODE----------------------------------
#initializing needed variables
clear()
answer = "y"


#start of loop - will be based on answer, and user can change value at end of loop
while answer == "y" or answer=="Y":
    print("\tWelcome to the Fire Department fire saftey program!")
    print(input("\tPlease enter your meeting name:"))
    print(input("\tHow many people are attending this meeting?"))
    print(input("\tWhat is the maximun capacity for that room?"))