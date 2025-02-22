# Robert Blye
# SE126.02
# Lab 5
# 2-14-25

# PROGRAM PROMPT:  to assign passengers seats in an airplane. The program should display the seat pattern, with an ‘X’ making the seats already assigned. After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated. This continues until all seats are filled or until the user signals that the program should end. If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.

# VARIABLE DICTIONARY:

# search_num = search by libary number

#----imports-------------------------------

import time
import csv
#----functions-------------------------------

def display_seating_chart():
    print("Airplane Seating Chart:")
    for i in range(len(rowNum)):
        print(f"{rowNum[i]} | {seatA[i]} {seatB[i]} {seatC[i]} {seatD[i]}")


#--create lists------------------------------

# Define the lists
rowNum = ["1", "2", "3", "4", "5", "6", "7"]
seatA = ["A", "A", "A", "A", "A", "A", "A"]
seatB = ["B", "B", "B", "B", "B", "B", "B"]
seatC = ["C", "C", "C", "C", "C", "C", "C"]
seatD = ["D", "D", "D", "D", "D", "D", "D"]

# Create or open a text file in write mode ('w')
with open('airplane_seating.txt', 'w') as file:
    # Write a header line to the file (optional)
    file = open('text_files/airplane_seating.csv' , 'w') # create text file 

for i in range(0, len(rowNum)):
    file.write(f"{rowNum[i]},{seatA[i]},{seatB[i]},{seatC[i]},{seatD[i]}\n") # data for text file \n will add them to a new line at the end
file.close() # close the file


display_seating_chart()
seat_input = input("Enter the seat to reserve: ")

