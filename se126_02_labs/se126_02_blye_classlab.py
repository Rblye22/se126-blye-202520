# Robert Blye
# SE126.02
# Week 4 - Class Lab
# 1-27-25

# PROGRAM PROMPT: to display a list of students first names, last names, scores from test 1, 2, and 3, and display average test scores and average letter grade. the program then gives the user a menu to make a choice of different search methods by last name, first name, letter grade or allow the user to choose to exit the program from the menu. the program also asks the user if they want to do another search after they have recieved the data allowing for a second escape in the loop. 

# VARIABLE DICTIONARY:
# firstName - first name of student
# lastName - last name of student
# test1 - score for test 1
# test2 - score for test 2
# test3 - score for test 3
# num_avg - average test score grade ( test1[i] + test2[i] + test3[i] ) / 3
# let_avg - is a letter grade assigned to the score used in the fuction
# def letter(num) - is a function that takes avg test score and takes that number and asigns it a letter grade
# search_name - name tof student that is being searched
# search_grade - letter grade that is being 
# search_type - is number choice from the menu to classify what search you want to perform
# let - letter grade for avg test scores
# found - variable used for condionals. It is used as a key if data has been found in the index
# num - the number of the avg grade 

#----imports-------------------------------

import csv

#----Functions-----------------------------

def letter(num):
    if num >= 90: # this is the grade value for A
        let ="A"
    elif num >= 80: # this the the grade value for B
        let = "B"
    elif num >= 70: # this is the grade value for C
        let = "C"
    elif num >= 60: # this is grade value for D
        let = "D"
    elif num < 60: # this is grade value for F
        let = "F"
    else:
        let = "ERROR" # this is entered choice is not a grade 

    return let # 'let' value replaces the func call in the main executing code

#create empty lists to hold the file data
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

# opens the text file
with open ("text_files/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

# disconnected from file -- can still acess stored data via the list

# process the list data to calc an avg score for each student, and find a letter grade equivalent

num_avg = [] # holds each students num avg of test scores
let_avg = [] # holds each students let acg of test scores

for i in range(0,len(firstName)):

    a = (test1[i] + test2[i] + test3[i]) / 3
    #add avg to num_avg list
    num_avg.append(a) 

    l = letter(a) # reurn value of letter() stored to i
    let_avg.append(l) 

# process the lists to diaplay all data back to the user
for i in range(0, len(firstName)):
    print(f"{firstName[i]:10}   {lastName[i]:10}   {test1[i]:3}   {test2[i]:3}   {test3[i]:3}   {num_avg[i]:6.2f}\t {let_avg[i]:6}")

print("-------------------------------------------------------------------------")

print(f"There are {len(firstName)} Students in the file.")

# Write a program that allows users repeaded searches

print("\n\n Welcome to the Student Search Program\n\n")

answer = input("would you like to begin searching? [y/n]: ").lower() #asking user to begin

while answer == "y":

    # get search type from user
    print("\tSearch Menu Options") 
    print("1. Search by LAST NAME") # search by last name
    print("2. Search by FIRST NAME") # search by first name
    print("3. Search by LETTER GRADE") # search by letter grade
    print("4. Exit") # exit program

    search_type = input("Enter your search type [1-4]: ") # users input of choice

    if search_type == "1":
        print("SEARCH BY LAST NAME") 
        
        found = -1 # invalid index, will check later to see if a student has been found

        # get search item from user
        search_name = input("Enter the LAST NAME of the student you are searching for: ")

        # perform search
        for i in range(0, len(lastName)):
            if search_name.lower() == lastName[i].lower():  
                found = i # make found the current index, can be used later to display

        # display the results
        if found!= -1:
            # last name has been found and display data
            print(f"Your search for {search_name} was Found")
            print(f"{firstName[found]:10}   {lastName[found]:10}   {test1[found]:3}   {test2[found]:3}   {test3[found]:3}   {num_avg[found]:6.2f} {let_avg[found]}")
        else:
            print(f"Your search for {search_name} was *NOT* FOUND!") # invalid response
            print(f"THIS is a cAsE sensative program - check your spelling and try again!") # case sensative

    if search_type == "2":
        print("SEARCH BY FIRST NAME")
        
        found = -1 #invalid index, will check later to see if a student has been found

        # get search item from user
        search_name = input("Enter the FIRST NAME of the student you are searching for: ")

        # perform search
        for i in range(0, len(firstName)):
            if search_name.lower() == firstName[i].lower():  
                found = i # make found the current index, can be used later to display

        #display the results
        if found!= -1:
            # First name has been found and display data
            print(f"Your search for {search_name} was Found")
            print(f"{firstName[found]:10}   {lastName[found]:10}   {test1[found]:3}   {test2[found]:3}   {test3[found]:3}   {num_avg[found]:6.2f} {let_avg[found]}")
        else:
            print(f"Your search for {search_name} was *NOT* FOUND!") # invalid response
            print(f"THIS is a cAsE sensative program - check your spelling and try again!") # case sensative
        
    elif search_type == "3":
        print("\tSearch by LETTER GRADE")
        found = [] #created empty list to gather and store index values

        # get search item from user
        search_grade = input("Enter the grade you wish to search for: ")

        # perform search
        for i in range(0, len(let_avg)):
            # the for loop allows "sequence" party -> to being to end
            if search_grade.upper() == let_avg[i]:
                # the IF STATEMNEt allows for "search" part
                found.append(i) # make found the current index, can be used later to display

        # display the results
        if not found: # this means list is empty
            print(f"Your search for {search_grade} was *NOT* FOUND!")
            print(f"THIS is a cAsE sensative program - check your spelling and try again!")

        else:
            print(f"Your search for {search_grade} was Found")

            # found is a list with mult. pieces of dtat - must use a for loop to see all
            for i in range(0, len(found)):
                # display list
                print(f"{firstName[found[i]]:10}   {lastName[found[i]]:10}   {test1[found[i]]:3}   {test2[found[i]]:3}   {test3[found[i]]:3}   {num_avg[found[i]]:6.2f} {let_avg[found[i]]}")

    # exit choice from menu 
    elif search_type == "4":
        answer = "n"
        print("Thank you for using the program!")
    
    if search_type == "1" or search_type == "2" or search_type == "3": # only user doesnt specify 3 to exit
        answer = input("would you like to search again? [y/n]: ").lower()

        
        
