#Robert Blye
#SE126.02
#in_class_lab - TextFile Handeling w/ Filters!
#1-14-2025 [W2D1]

#PROGRAM PROMPT: 
# the program is to display the amount of rooms that are over capacity and display the amount of people it is over by.


#VARIABLE DICTIONARY:
# difference - is the function that does subtraction to see how many people the room is over capacity
# max_cap - max capacity for the room
# people - people registered for the event
# rooms_over - the amount of rooms over capacity
# name - is the name of the room
# total_records - the total amount of records being displayedd from the list
# remaining - is the the result of the subtraction in the difference function

#--------------Imports------------------
import csv

#----------Functions-----------------------------

def difference(max_cap, people):
    '''This is a subtraction function'''
    diff = max_cap - people 
    return diff

    
#-------Header--------------------
print(f"\n{'Name':10}    \t\t   {'MAX':3}    {'People':5}     {'OVER'}")
#HEADER PRINT
print("-------------------------------------------------")

#--------Main Code----------------------------------
#initialize neede counting variables

total_records = 0 #the total number of recors (rows) in the file
rooms_over = 0 #number of roooms over

#----------Connected to file-----------

with open("text_files/classLab2.csv") as csvfile:

     file = csv.reader(csvfile)

     for record in file:

        total_records += 1

        #print(record) #this is the list view of each record (row)

        #assign each field data to a friendly var name
    
        name = record [0]
        max_cap = int(record[1]) #all text data read as a string, cast as int
        people = int(record[2])

        #call the fuction diff()
        remaining = difference(people, max_cap)

        #count and display rooms over capacity (remaining is negative)

        if remaining > 0:
            rooms_over += 1
            print(f" {name:20}     {max_cap:5}   {people:5}    {abs(remaining):5}") # abs func or * by - 1

   

#----------Connected to file-----------

print(f"\nRooms currently over capacity: {rooms_over}")
print(f"Total rooms in the file: {total_records} \n\n")
