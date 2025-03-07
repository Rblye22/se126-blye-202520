# Robert Blye
# SE126.02
# Final 
# 3/1/2025

# PROGRAM PROMPT: The program must either utilize a file or create an edited file. The program must include at minimum the use of at least two 1D lists or one 2D list. The program must showcase an understanding of control flow structures: repetition and single-decision. The program must showcase an understanding of self-built functions, to include the need for parameters as well as return values. The program must include the use of a searching algorithm: either sequential or binary (or both). The program must import at least one python library documentation include a brief program description at the start of the file include internal documentation related to the functionality of your program code documentation for anything used not introduced in the course.

# VARIABLE DICTIONARY:
# callsign = A call sign is a unique identifier used in radio communication to distinguish one station or operator from another.
# unit = The Unit of the call sign (ex. 2-70 is 2nd battalion 70th armored regigement)
# radio_freq = the frequency that the unit is on for their communications
# unit_type = type of unit they are (ex. Infantry or Tank)

#----imports-----------------------------------------------------------------------
import time
import csv
import os
#--functions-------------------------------------------------------------------------
def clear():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/MacOS
        os.system('clear')

def display(x, foundList, records):
    '''
        PARAMETERS:
            x   signifier for if we are printing a single record or multiple
                when x != "x" it is an integere index and we have one value, otherwise we have multiple
            records the length of a list we are going to process through (# of loops/prints)
    '''
    print(f"\n{'CALLSIGN':15}\t{'UNIT':6}\t  {'RADIO FREQ':12}\t   {'UNIT TYPE'}")
    print("-" * 70)
    if x != "x":
        #printing one record
        print(f"{callsign[x]:15}   {unit[x]:12}  {radio_freq[x]:14}  {unit_type[x]}")
    elif foundList:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{callsign[foundList[i]]:15}  {unit[foundList[i]]:10}  {radio_freq[foundList[i]]:12} {unit_type[foundList[i]]}")
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{callsign[i]:15}  {unit[i]:10}  {radio_freq[i]:12}  {unit_type[i]}")

#--create csv file-------------------------------------------------------------------
callsign = ["ArchAngel", "Bayonet", "Choas", "Demon", "Shadow", "Thunder Actual"] # unit call sign
unit = ["2-70", "1-18", "1-63", "1-7", "5-4", "2-70"] # unit
radio_freq = ["138.00", "139.00", "140.00", "141.00", "142.00", "143.00"] # radio frequency
unit_type = ["Infantry", "Infantry", "Tank", "Artillery", "Scout", "Battalion-HQ"] # type of unit

#--create a csv file---------------------------------------------------------
file = open("text_files/radio_check.csv", "w") # create text file 

for i in range(0, len(callsign)):
    if i == len(callsign) -1:
        file.write(f"{callsign[i]},{unit[i]},{radio_freq[i]},{unit_type[i]}")
    else:
        file.write(f"{callsign[i]},{unit[i]},{radio_freq[i]},{unit_type[i]}\n")
file.close() # close the file

clear()

print("\n\tWelcome to the 1st Infantry Division Radio Communications Sytem!")
time.sleep(2)
answer = "y"
search_type = 0
while answer.lower() == "y" and search_type != 4:

    # get search type from user
    print("\n\tSearch Menu Options\n")
    print("\t1. Show all Units and their information") # show all titles
    print("\t2. Search by Callsign") # search by title
    print("\t3. Search by Unit") # search by author
    print("\t4. Search by Frequency") # search by genre
    print("\t5. Search by Unit Type") # search by number
    print("\t6. Exit") # exit program

    search_type = input("\n\tEnter your search type [1-6]: ") # users input of choice

        #using 'not in' for user validity checks
    if search_type not in ["1", "2", "3", "4","5","6"]:
        print("***INVALID ENTRY!***\nPlease try again")

    elif search_type == "1":
        print(f"\n{'CALLSIGN':15}\t{'UNIT':4}\t{'RADIO FREQ':10}\t{'UNIT TYPE'}")
        print("-" * 70)
        for i in range(len(callsign)):
            print(f"{callsign[i]:15}\t{unit[i]:4}\t{radio_freq[i]:10}\t{unit_type[i]}")
            time.sleep(.5)
        print("-" * 70)

    elif search_type == "2":
        print(f"\nYou have chosen to search by Callsign\n")
        search = input("Which Callsign are you looking for: ").lower()
        found = []
        # 
        for i in range(0, len(callsign)):
            if search.lower() in callsign[i].lower():
                found.append(i)

        if not found: 
            print(f"Sorry, we have no Callsign {search} assigned to us")
        else:
            display("x", found, len(found))
            time.sleep(2)

    elif search_type == "3":
        print(f"\nYou have chosen to search by Unit\n")
        print("Please enter the unit as Battion - Regiment (ex.2-16)\n")
        search = input("What Unit are you looking for: ")
        
        found = []
        # 
        for i in range(0, len(unit)):
            if search in unit[i]:
                found.append(i)
        if not found: 
            print(f"Sorry, {search} is not assigned to us")
        else:
            display("x", found, len(found))
            time.sleep(2)
            
    elif search_type == "4":
        print(f"\nYou have chosen to search by Radio Frequency\n")
        search = input("What Radio Frequency are you looking for: ")
        found = []
        # 
        for i in range(0, len(radio_freq)):
            if search in radio_freq[i]:
                found.append(i)
        if not found: 
            print(f"Sorry, {search} is not assigned to us")
        else:
            display("x", found, len(found))
            time.sleep(2)

    elif search_type == "5":
        print(f"\nYou have chosen to search by Unit Type\n")
        search = input("What Unit are you looking for: ")
        found = []
        # 
        for i in range(0, len(unit_type)):
            if search.lower() in unit_type[i].lower():
                found.append(i)

        if not found: 
            print(f"Sorry, {search} is not assigned to us")
        else:
            display("x", found, len(found))
            time.sleep(2)
    
    # exit choice from menu 
    elif search_type == "6":
        answer = "n" # exit the loop
        print("\nThank you for using the 1st Infantry Division Radio Communications Sytem!\n")