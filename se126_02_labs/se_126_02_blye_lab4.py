# Robert Blye
# SE126.02
# Lab 4
# 1-28-25

# PROGRAM PROMPT: Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension. When you are complete, display the following data for each employee (first name, last name, department, email, and phone extension) to the user. Use the following field width guide to avoid unaligned field displays:Once you have completed populating all eight parallel lists and displaying the five required back to the user (and in the same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. note: each employee’s data should be on its own record (row) within the newly created file. You will most likely end up with an extra empty line at the end of the file (this is okay for this lab as we will not be reprocessing the data found in this new file). Once the file is ready, close it and alert the user via a displayed message. Also tell them how many employees are in the file, and the total count of employees for each department. 

# use this display to print - print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")

# VARIABLE DICTIONARY:
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

#----imports-------------------------------

import csv
import random

#--Initalize for function------------------
dep = []
ext = []
email_add = []

#----Functions-----------------------------
def houseA(house):
    if house >= 100 or house <= 199:
        print("House Stark")
    
    if house >= 200 or house <= 299:
        print("House Targaryen")

    if house >= 300 or house <= 399:
        print("House Tully ")

    if house >= 400 or house <=499:
        print("House Lannister")

    if house >=500 or house <= 599:
        print("House Baratheon")
    
    if house >= 600 or house <= 699:
        print("The Night’s Watch")

    if house <100 or house >= 700:
        house = "Error"

    return house
    


def depart():
    if dep >= 100 or dep <= 199:
        print("Research and Development")
    
    if dep >= 200 or dep <= 299:
        print("Marketing")

    if dep >= 300 or dep <= 399:
        print("Human Resources")

    if dep >= 400 or dep <= 499:
        print("Accounting")

    if dep >= 500 or dep <= 599:
        print("Sales ")

    if dep >= 600 or dep <= 600:
        print("Auditing ")

    return dep[i]


def phone(ext):
    for i in range(100, 199):
        ext1 = random.randit(100, 199)
        print(f"The phone extension is {ext1}")
    
    for i in range(200, 299):
        ext2 = random.randit(200, 299)
        print(f"The phone extension is {ext2}")

    for i in range(300, 399):
        ext3 = random.randit(300, 399)
        print(f"The phone extension is {ext3}")

    for i in range(400, 499):
        ext4 = random.randit(400, 499)
        print(f"The phone extension is {ext4}")

    for i in range(500, 599):
        ext5 = random.randit(500, 599)
        print(f"The phone extension is {ext5}")

    for i in range(600, 699):
        ext6 = random.randit(600, 699)
        print(f"The phone extension is {ext6}")

    else:
        ext = "ERROR" 

    return ext[i]

def emails():
    email_add = scrnName[i]+ "@Westeros.net"

    return email_add[i]

#--Main Executing Code----------------------------

#create empty lists - one for each field
fName = []
lName = []
age = []
scrnName =[]
house = []
email_add = []
dep = []
ext = []


#--EMAIL ADDRESS-----------------------------------------



# opens the text file
with open ("text_files/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(int(rec[2]))
        scrnName.append(rec[3])
        house.append(rec[4])
        
    #--disconected from file-----------------------------


print("-------------------------------------------------------------------------------------------")

# Write a program that allows users repeaded searches

print("Welcome to the employee database!")

answer = input("would you like to begin searching? [y/n]: ").lower() #asking user to begin

while answer == "y":

    # get search type from user
    print("\tSearch Menu Options") 
    print("1. Search by FIRST NAME") # search by first name
    print("2. Search by PHONE EXTENSION") # search by phone extension
    print("3. Search by LAST NAME") # search by last name
    print("4. Search by DEPARTMENT") # search by department
    print("5. Exit") # exit program

    search_type = input("Enter your search type [1-5]: ") 

    if search_type == "1":
        print("SEARCH BY FIRST NAME") 
        
        found = -1 

        # get search item from user
        search_fName = input("Enter the LAST NAME of the employee you are searching for: ").lower()

        # perform search
        for i in range(0, len(fName)):
            if search_fName.lower() == fName[i].lower():  
                found = i # make found the current index

        # display the results
        if found!= -1:
            # first name has been found and display data
            print(f"Your search for {search_fName} was Found")
            print(f"{fName[found]:10}   {lName[found]:10}   {age[found]:3}   {scrnName[found]:3}   {house[found]:3}   {email_add[found]:6.2f} {dep[found]} {ext[found]}")
        else:
            print(f"Your search for {search_fName} was *NOT* FOUND!") # invalid response
            print(f"THIS is a cAsE sensative program - check your spelling and try again!") # case sensative

    if search_type == "2":
        print("SEARCH BY Phone Extension")
        
        found = -1 #invalid index, will check later to see if a student has been found

        # get search item from user
        search_name = input("Enter the phone extension you are searching for: ")

        # perform search
        for i in range(0, len(age)):
            if search_name == ext[i]:
                found = i # make found the current index, can be used later to display

        #display the results
        if found!= -1:
            # First name has been found and display data
            print(f"Your search for {search_name} was Found")
            print(f"{fName[found]:10}   {lName[found]:10}   {age[found]:3}   {scrnName[found]:3}   {house[found]:3}   {email_add[found]:6.2f} {dep[found]} {ext[found]}")
        else:
            print(f"Your search for {search_name} was *NOT* FOUND!") # invalid response
            print(f"THIS is a cAsE sensative program - check your spelling and try again!") # case sensative
        
    elif search_type == "3":
        print("\tSearch by LAST NAME")
        found = [] #created empty list to gather and store index values

        # get search item from user
        search_lName = input("Enter the department you wish to search for: ")

        # perform search
        for i in range(0, len(lName)):
            # the for loop allows "sequence" party -> to being to end
            if search_lName.lower() == lName[i]:
                # the IF STATEMNEt allows for "search" part
                found.append(i) # make found the current index, can be used later to display

        # display the results
        if not found: # this means list is empty
            print(f"Your search for {search_lName} was *NOT* FOUND!")
            print(f"THIS is a cAsE sensative program - check your spelling and try again!")

        else:
            print(f"Your search for {search_lName} was Found")

            # found is a list with mult. pieces of dtat - must use a for loop to see all
            for i in range(0, len(found)):
                # display list
                print(f"{fName[found]:10}   {lName[found]:10}   {age[found]:3}   {scrnName[found]:3}   {house[found]:3}   {email_add[found]:6.2f} {dep[found]} {ext[found]}")

    elif search_type == "4":
        print("\tSearch by DEPARTMENT")
        found = [] #created empty list to gather and store index values

        # get search item from user
        search_dep = input("Enter the Department you wish to search for: ")

        # perform search
        for i in range(0, len(age)):
            # the for loop allows "sequence" party -> to being to end
            if search_dep.lower() == dep[i].lower():
                # the IF STATEMNEt allows for "search" part
                found.append(i) # make found the current index, can be used later to display

        # display the results
        if not found: # this means list is empty
            print(f"Your search for {search_dep} was *NOT* FOUND!")
            print(f"THIS is a cAsE sensative program - check your spelling and try again!")

        else:
            print(f"Your search for {search_dep} was Found")

            # found is a list with mult. pieces of dtat - must use a for loop to see all
            for i in range(0, len(found)):
                # display list
                print(f"{fName[found]:10}   {lName[found]:10}   {age[found]:3}   {scrnName[found]:3}   {house[found]:3}   {email_add[found]:6.2f} {dep[found]} {ext[found]}")


    # exit choice from menu 
    elif search_type == "5":
        answer = "n"
        print("Thank you for using the program!")
    
    if search_type == "1" or search_type == "2" or search_type == "3": # only user doesnt specify 3 to exit
        answer = input("would you like to search again? [y/n]: ").lower()