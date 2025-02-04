# Robert Blye
# SE126.02
# Midterm pt. 2
# 2/4/2025

# PROGRAM PROMPT: Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold a “status” value for each book. Assign each book a status value of “On Loan” or “Available” and store to the newly created list. Half of the books should be “On Loan” and the other half should be “Available” – you can decide which books hold which status as long as it is an even split between the two potential values. Once the new list is populated, process through the five lists to display all of the data to the user as well as the total number of records in the file. Once all of the data has been displayed, write all of the list data to a new file called ‘midterm_choice2.csv’, where each book’s information is found on one record in the file and their data is separated by a comma (additional empty line in resulting file is okay). Finally, create a sequential search program that allows a user to repeatedly search the book database information stored in the lists based on the following menu:

# VARIABLE DICTIONARY:
# clear() = function to clear terminal
# time.sleep(x) = used to freeze the terminal for x amount of seconds
# ol_total = total for books on loan
# avail_total = total books available
# total_rec = total amount of books in the file
# title = title of the book
# author = the person who wrote the book
# genre = type of category the book is in
# pages = the number of pages in the book
# status = if the book is available or on loan
# search_title = search by title
# search_aut = search by author
# search_type = type of search the program is running

#----imports-------------------------------

import time
import csv
import os

#----functions-------------------------------

def clear():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/MacOS
        os.system('clear')

#--initialize---------------------------------------

ol_total = 0
avail_total = 0 
total_rec = 0
#--create empty lists------------------------------

title = []
author = []
genre = []
pages = []
status = []

# opens the text file
with open ("text_files/books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists

        total_rec += 1 
        # total record counter

        title.append(rec[0]) # first name append
        author.append(rec[1]) # last name append
        genre.append(rec[2]) # age append
        pages.append(rec[3]) # screen name append
        
    #--disconected from file-----------------------------
clear()


print("------------------------------------------------------------------------------------------------------------")

for i in range(len(title)):

    if title[i] == "Tigana": # title
        status.append("on loan") # Lucy Foley
        ol_total += 1

    elif title[i] == "Ninth House": # title
        status.append("available") # status
        avail_total += 1 

    elif title[i] == "Holly": # title
        status.append("available") # status
        avail_total += 1

    elif title[i] == "The Outsider": # title
        status.append("on loan") # status
        ol_total += 1

    elif title[i] == "The House Across the Lake": # title
        status.append("available") # status
        avail_total += 1

    elif title[i] == "The Warm Hands of Ghosts": # title
        status.append("available") # status
        avail_total += 1

    elif title[i] == "The Midnight Feast": # title
        status.append("on loan") #status
        ol_total += 1

    elif title[i] == "The Hunting Party": # title
        status.append("on loan") # status
        ol_total += 1

    elif title[i] == "Wool": # title
        status.append("on loan") # status
        ol_total += 1

    elif title[i] == "Shift": # title
        status.append("available") # status
        avail_total += 1

    elif title[i] == "Dust": # title
        status.append("available") # status
        avail_total += 1
    
    elif title[i] == "The Echo Wife": # title
        status.append("on loan") # status
        ol_total += 1
    
    else:
        title[i] == "Just Like Home" # title
        status.append("available") # status
        avail_total += 1

#--print header--------------------------------------------------
print(f"{'TITLE':10}\t\t\t{'Author':10}\t\t\t{'Grenre':10}\t\t{'Pages':10} {'STATUS':8}")

print("------------------------------------------------------------------------------------------------------------")

# print data from the lists
for i in range(len(title)):
    print(f"{title[i]:30}\t {author[i]:20}\t\t{genre[i]:10}\t\t{pages[i]:3}\t {status[i]:8}")

print("------------------------------------------------------------------------------------------------------------")

time.sleep(1) # sleep timer for display

print(f"\n\t\tThere are {total_rec} books in our libary\n") # total number of books in the file


file = open('text_files/midterm_choice2.csv' , 'w') # create text file 

for i in range(0, len(title)):
    file.write(f"{title[i]},{author[i]},{genre[i]},{pages[i]},{status[i]}\n") # data for text file \n will add them to a new line at the end
file.close() # close the file

time.sleep(1) # sleep timer for display

print("\nWelcome to the libary search program\n")

answer = input("\nwould you like to begin searching? [y/n]: ").lower() #asking user to begin

while answer == "y":

    # get search type from user
    print("\tSearch Menu Options\n") 
    print("1. Search by Title") # search by title
    print("2. Search by Author") # search by author
    print("4. Exit") # exit program

    search_type = input("\nEnter your search type [1-3]: \n") # users input of choice

    if search_type == "1":
        print("Search by Title") 
        
        found = -1 # invalid index, will check later to see if the title has been found

        # get search item from user
        search_title = input("\nEnter the title of the book you are searching for: ")

        # perform search
        for i in range(0, len(title)):
            if search_title.lower() == title[i].lower():  
                found = i # make found the current index, can be used later to display

        # display the results
        if found!= -1:
            # title has been found and display data
            print(f"\nYour search for {search_title} was Found")
            print(f"{title[found]:30}\t {author[found]:20}\t\t{genre[found]:10}\t\t{pages[found]:3}\t {status[found]:8}")
        else:
            print(f"\nYour search for {search_title} was *NOT* FOUND!") # invalid response
            print(f"THIS is a cAsE sensative program - check your spelling and try again!") # case sensative

    if search_type == "2":
        print("Search by Author")
        found = [] #created empty list to gather and store index values

        # get search item from user
        search_aut = input("\nEnter the grade you wish to search for: ")

        # perform search
        for i in range(0, len(author)):
            if search_aut.lower() == author[i].lower():
                found.append(i) # make found the current index, can be used later to display

        # display the results
        if not found: # this means list is empty
            print(f"\nYour search for {search_aut} was *NOT* FOUND!")
            print(f"THIS is a cAsE sensative program - check your spelling and try again!")

        else:
            # search was found
            print(f"\nYour search for {search_aut} was Found")

            # found is a list with mult. pieces of dtat - must use a for loop to see all
            for i in range(0, len(found)):
                # display list
                print(f"{author[found[i]]:30}   {title[found[i]]:20}   {genre[found[i]]:10}   {pages[found[i]]:3}   {status[found[i]]:8}")


    # exit choice from menu 
    elif search_type == "3":
        answer = "n" # exit the loop
        print("\nThank you for using the program!\n")
    
    if search_type == "1" or search_type == "2": # only user doesnt specify 3 to exit
        answer = input("\nwould you like to search again? [y/n]: ").lower()
