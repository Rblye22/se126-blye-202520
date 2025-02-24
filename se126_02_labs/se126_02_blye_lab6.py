# Robert Blye
# SE126.02
# Lab 6
# 2-23-25

# PROGRAM PROMPT: to assign passengers seats in an airplane. The program should display the seat pattern, with an ‘X’ making the seats already assigned. After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated. This continues until all seats are filled or until the user signals that the program should end. If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.

# VARIABLE DICTIONARY:
# display_seating_chart() = function used to display the seating chart
# update_seat() = function used to see if a seat is available or to reserve a seat
# save_seating_chart() = function to save seating chart as csv file
# rowNum = row number in the plane\
# seat = seat letter A - D
# row = row number on the flight
# seat_input = the input the user is choosing for row and seat number (1A)
# seatA = seat A in the plane for the fight (WINDOW SEAT)
# seatB = seat B in the plane for the flight (ISLE SEAT)
# seatC = seat C in the plane for the flight (ISLE SEAT)
# seatD = seat D in the plane for the flight (WINDOW SEAT)
# continue_reservation = ask the user if they have another reservation if no it exits the program

#--Imports----------------------------------------------

import time
import csv

#--Functions---------------------------------------------

def display_seating_chart():
    print("\t         __|__")
    print("\t  --@--@--(_)--@--@--")
    print("\n\tAirplane Seating Chart\n")
    time.sleep(1)
    
    print(f"\t{'ROW':10}{'SEATS A - D'}")
    print("---------------------------------------")
    for i in range(len(rowNum)):
        print(f"\t{rowNum[i]}    (_)  {seatA[i]} {seatB[i]} |   | {seatC[i]} {seatD[i]} (_)")  # (_) is a window |  | is isle

def update_seat(seat_input):
    #Update the seat reservation
    row = seat_input[0]
    seat = seat_input[1]

    for i in range(len(rowNum)):
        if rowNum[i] == row:
            if seat == "A" and seatA[i] != "X":
                seatA[i] = "X"
                print(f"\n\tSeat {seat_input} has been selected!\n")
            elif seat == "B" and seatB[i] != "X":
                seatB[i] = "X"
                print(f"\n\tSeat {seat_input} has been selected!\n")
            elif seat == "B" and seatC[i] != "X":
                seatC[i] = "X"
                print(f"\n\tSeat {seat_input} has been selected!\n")
            elif seat == "D" and seatD[i] != "X":
                seatD[i] = "X"
                print(f"\n\tSeat {seat_input} has been selected!\n")
            else:
                print(f"\n\tSeat {seat_input} is already taken or invalid!\n")
            return
    print("\tInvalid seat input!\n")

def save_seating_chart():
    #Save the seating chart to a file.
    with open("text_files/airplane_seating.csv", "w") as file:
        for i in range(len(rowNum)):
            file.write(f"{rowNum[i]}, {seatA[i]}, {seatB[i]}, {seatC[i]}, {seatD[i]}\n")

def goAgain():
    #ask the user to reserve another seat or exit
    return input("Would you like to reserve another seat on this flight? [y/n]: ").lower()

#--Create lists for rows and seats-------------------------------------------
rowNum = ["1", "2", "3", "4", "5", "6", "7"] # row numbers
seatA = ["A", "A", "A", "A", "A", "A", "A"]
seatB = ["B", "B", "B", "B", "B", "B", "B"]
seatC = ["C", "C", "C", "C", "C", "C", "C"]
seatD = ["D", "D", "D", "D", "D", "D", "D"]

#--create a csv file---------------------------------------------------------
file = open("text_files/airplane_seating.csv", "w") # create text file 

for i in range(0, len(rowNum)):
    file.write(f"{rowNum[i]},{seatA[i]},{seatB[i]},{seatC[i]},{seatD[i]}\n") # data for text file \n will add them to a new line at the end
file.close() # close the file

#--Main Executing Code------------------------------------------------------
valid_seats = ['A', 'B', 'C', 'D'] # seats A - D are valid
continue_reservation = "y"

while continue_reservation == "y":
    display_seating_chart()  # Show seating chart
    seat_input = input("\n\tEnter the seat to reserve: ").upper()  # Ask user for seat choice

    if len(seat_input) == 2 and seat_input[0] in rowNum and seat_input[1] in valid_seats:
        update_seat(seat_input)  # Update the seat
        save_seating_chart()  # Save updated seating chart after reservation was made
    else:
        print("Invalid seat input, please try again!\n") # invalid response

    # Call the function to ask if the user wants to reserve another seat or exit
    continue_reservation = goAgain()

print("\n\tThank you for using our reservation system\n\t\t Goodbye!")