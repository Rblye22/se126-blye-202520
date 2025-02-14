# Robert Blye
# SE126.02
# Lab 5
# 2-14-25

# PROGRAM PROMPT: Build a personal library search system using the file book_list.csv. Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options. When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author, Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches should not be case sensitive.

# VARIABLE DICTIONARY:
# libNum = libary number
# title = book title
# author = author of the book
# genre = genre of book (ex. horror)
# pages = number of pages in the book
# status = status if the book is on loan or available
# temp = temp place holder for sorting 
# listname = list name used for swapping data to organize
# search_type = type of search the user chooses
# search_aut = search by name of author
# search_gen = search by genre
# search_num = search by libary number

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

def display(x, foundList, records):
    '''
        PARAMETERS:
            x   signifier for if we are printing a single record or multiple
                when x != "x" it is an integere index and we have one value, otherwise we have multiple

            records   the length of a list we are going to process through (# of loops/prints)
    '''
    print(f"{'Libary #':8}    {'TITLE':40}  {'Author':20}\t{'Grenre':15} {'Pages':13}\t{'STATUS':4}")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{libNum[x]:8}  {title[x]:40}  {author[x]:20}  {genre[x]:20} {pages[x]:13} {status[x]:10}") 

    elif foundList:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{libNum[foundList[i]]:8}  {title[foundList[i]]:40}  {author[foundList[i]]:20} {genre[foundList[i]]:20} {pages[foundList[i]]:13} {status[foundList[i]]:10}") 
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{libNum[i]:8}  {title[i]:40}  {author[i]:20}  {genre[i]:20} {pages[i]:13} {status[i]:10}") 

    print("-------------------------------------------------------------------------------------------------------------------------------\n")

def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp
#--initalize---------------------------------------
total_avail = 0
total_loan = 0
#--create empty lists------------------------------

libNum =[]
title = []
author = []
genre = []
pages = []
status = []

found = []

# opens the text file
with open ("text_files/book_list.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists
        # total record counter
        libNum.append(rec[0]) # libary number append
        title.append(rec[1]) # first name append
        author.append(rec[2]) # last name append
        genre.append(rec[3]) # age append
        pages.append(rec[4]) # screen name append
        status.append(rec[5])
        
    #--disconected from file-----------------------------
clear()

print("\n\tWelcome to the libary search program!!\n")
time.sleep(2)
answer = "y"
search_type = 0
while answer.lower() == "y" and search_type != 4:

    # get search type from user
    print("\tSearch Menu Options\n")
    print("\t1. Show all Titles") # show all titles
    print("\t2. Search by Title") # search by title
    print("\t3. Search by Author") # search by author
    print("\t4. Search by Genre") # search by genre
    print("\t5. Search by Libary Number") # search by number
    print("\t6. Show All Available ") # show available
    print("\t7. Show All on Loan ") # show on loan
    print("\t8. Exit") # exit program

    search_type = input("\nEnter your search type [1-8]: \n") # users input of choice

        #using 'not in' for user validity checks
    if search_type not in ["1", "2", "3", "4","5","6", "7", "8"]:
         print("***INVALID ENTRY!***\nPlease try again")

    elif search_type == "1":
        print(f"\nYou have chosen to show all Tiles\n")
        #BUBBLE SORT ALGORITHM
        for i in range(0, len(title) - 1):#outter loop
                #print("OUTER LOOP! i = ", i)

                for index in range(0, len(title) - 1):#inner loop
                    #below if statement determines the sort
                    #list used is the list being sorted
                    # > is for increasing order, < for decreasing

                    if(title[index] > title[index + 1]):

                        #if above is true, swap places!
                        temp = title[index]
                        title[index] = title[index + 1]
                        title[index + 1] = temp

                        #swap all other values
                        temp = libNum[index]
                        libNum[index] = libNum[index + 1]
                        libNum[index + 1] = temp

                        temp = author[index]
                        author[index] = author[index + 1]
                        author[index + 1] = temp

                        temp = genre[index]
                        genre[index] = genre[index + 1]
                        genre[index + 1] = temp

                        temp = pages[index]
                        pages[index] = pages[index + 1]
                        pages[index + 1] = temp

                        temp = status[index]
                        status[index] = status[index + 1]
                        status[index + 1] = temp

        print("\t\tTITLES BY ALPHABETICAL ORDER\n\n")
        print(f"{'Libary #':8}    {'TITLE':40}  {'Author':20}\t{'Grenre':15} {'Pages':13}\t{'STATUS':4}") # header
        print("-------------------------------------------------------------------------------------------------------------------------------")
        for i in range(0, len(title)):
            print(f"{libNum[i]:8}  {title[i]:40}  {author[i]:20}  {genre[i]:20} {pages[i]:13} {status[i]:10}") # display the lists in alphabetical order
        print("-------------------------------------------------------------------------------------------------------------------------------\n")
        time.sleep(2)

    elif search_type == "2":
        print(f"\nYou have chosen to search by Title\n")

        search = input("Which Title are you looking for:").lower()

        found = []
        #allow the program to search for parts of a name like 'dragon' or 'light'
        for i in range(0, len(title)):
            if search.lower() in title[i].lower():
                found.append(i)

        if not found: 
            print(f"Sorry, we have no names related to the meaning you entered: '{search}'")
        else:
            display("x", found, len(found))
            time.sleep(2)

    if search_type == "3":
        print("Search by Author\n")
        found = [] #created empty list to gather and store index values

        # get search item from user
        search_aut = input("\nEnter the author you wish to search for: ")

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
            print(f"\nYour search for {search_aut} was Found\n")

            # found is a list with mult. pieces of dtat - must use a for loop to see all
            for i in range(0, len(found)):
                # display list
                print(f"{libNum[found[i]]:8}  {title[found[i]]:40}  {author[found[i]]:20}  {genre[found[i]]:20} {pages[found[i]]:13} {status[found[i]]:10}")
                time.sleep(2)

    if search_type == "4":
        print(f"\nYou have chosen to search by Genre\n")
        found = [] #created empty list to gather and store index values

        # get search item from user
        search_gen = input("\nEnter the genre you wish to search for: ")

        # perform search
        for i in range(0, len(genre)):
            if search_gen.lower() == genre[i].lower():
                found.append(i) # make found the current index, can be used later to display

        # display the results
        if not found: # this means list is empty
            print(f"\nYour search for {search_gen} was *NOT* FOUND!")
            print(f"THIS is a cAsE sensative program - check your spelling and try again!")

        else:
            # search was found
            print(f"\nYour search for {search_gen} was Found\n")

            # found is a list with mult. pieces of dtat - must use a for loop to see all
            for i in range(0, len(found)):
                # display list
                print(f"{libNum[found[i]]:8}  {title[found[i]]:40}  {author[found[i]]:20}  {genre[found[i]]:20} {pages[found[i]]:13} {status[found[i]]:10}")
                time.sleep(2)

    if search_type == "5":
        print(f"\nYou have chosen to search by Libary Number\n")
        found = [] #created empty list to gather and store index values

        # get search item from user
        search_num = input("\nEnter the genre you wish to search for: ")

        # perform search
        for i in range(0, len(genre)):
            if search_num.lower() == libNum[i].lower():
                found.append(i) # make found the current index, can be used later to display

        # display the results
        if not found: # this means list is empty
            print(f"\nYour search for {search_num} was *NOT* FOUND!")
            print(f"THIS is a cAsE sensative program - check your spelling and try again!")

        else:
            # search was found
            print(f"\nYour search for {search_num} was Found\n")

            # found is a list with mult. pieces of dtat - must use a for loop to see all
            for i in range(0, len(found)):
                # display list
                print(f"{libNum[found[i]]:8}  {title[found[i]]:40}  {author[found[i]]:20}  {genre[found[i]]:20} {pages[found[i]]:13} {status[found[i]]:10}")
                time.sleep(2)

    if search_type == "6":
        search = "available" # set search to available status
        found = []
        if search.lower() == "on loan":
            print("\nYou have chosen to show all available books\n") # let user know their choice
           
        for i in range(0, len(status)):
            if status[i].lower() == search.lower():
                found.append(i)  # Add the index of the found item
            
            # Display results
        if not found:  # If no matches were found
            print(f"Sorry, your search for {search} came up empty")
        else:
            # Display the items that match the "on loan" status
            print(f"Books that are {search}:")
            for i in found:
                print(f"{libNum[i]:8}  {title[i]:40}  {author[i]:20}  {genre[i]:20} {pages[i]:13} {status[i]:10}")
        time.sleep(2)

    if search_type == "7":
        search = "on loan" # set search to on loan status
        found = []
        if search.lower() == "on loan": 
            print("\nYou have chosen to show all On Loan books\n") # let user know their choice
           
        for i in range(0, len(status)):
            if status[i].lower() == search.lower():
                found.append(i)  # Add the index of the found item
            
            # Display results
        if not found:  # If no matches were found
            print(f"Sorry, your search for {search} came up empty")
        else:
            # Display the items that match the "on loan" status
            print(f"Books that are {search}:")
            for i in found:
                print(f"{libNum[i]:8}  {title[i]:40}  {author[i]:20}  {genre[i]:20} {pages[i]:13} {status[i]:10}")
            time.sleep(2)

    # exit choice from menu 
    elif search_type == "8":
        answer = "n" # exit the loop
        print("\nThank you for using the program!\n")