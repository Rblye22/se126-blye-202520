# Robert Blye
# SE126.02
# Lab 7
# 2-27-25
# PROGRAM PROMPT: Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a user to interact with the dictionary based on the following menu: My Programming Dictionary Menu 1. Show all words – Show all words and their definitions stored to the dictionary 2. Search for a word – Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if the word is not in the dictionary) 3. Add a word – Allow a user to add a word and its definition to the dictionary if it does not already exist 4. EXIT The program should not be case sensitive for user input, and the user should only be able to quit when they have selected menu option number 4.

# VARIABLE DICTIONARY:
# library = Dictionary used to store words and their definitions both are strings
# search_type = the type of search the user is trying to use from the menu
# key = the word in the dictionary 
# add_word = add a word to the dictionary
# add_def = add definition of a word to the dictionary
# found = search result was found 

#--Imports----------------------------------------------------------
import csv
import time

#--Functions--------------------------------------------------------

#--Main Executing Code-----------------------------------------------

library = {
    # indexs are strings set by the dev
    #'key' : value
    "python" : "a popular programming language created by Guido van Rossum",
    "documentation" : "programming comments; notes within code which explain what the code does"
}

with open("text_files\words.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        # add each record data as a new key + value pair from the text file
        # key --> rec[0] ; value --> rec[1]
        library.update({rec[0] : rec[1]})
        # when using .update() --> pass {'key' : value}

#--disconnect from file----------------------------------------------------

print("\n\tWelcome to the Dictionary Search Program!\n") # welcome message
time.sleep(1)
answer = "y"
search_type = 0 # initializing search type
while answer.lower() == "y" and search_type != 4:
    # get search type from user
    print("\tSearch Menu Options\n")
    print("\t1. Show Dictionary") # show dictionary
    print("\t2. Search by Word") # search for word
    print("\t3. Add Word to Dictionary") # add word to dictionary
    print("\t4. Exit") # exit program

    search_type = input("\nEnter your search type [1-4]: \n") # users input of choice

        #using 'not in' for user validity checks
    if search_type not in ["1", "2", "3", "4"]:
        print("***INVALID ENTRY!***\nPlease try again") # invalid entry
    
    elif search_type == "1":
        print(f"\n\tYou have chosen to Show Dictionary\n\n")
        print(f"\n{'Word''-':20}\n{'DEFINITION'}")
        print("-" * 70) # print("---------------------------------------------------")
        for key in library:
    # loops runs for every key (and value) pair found within the libary dictionary
            print(f"{key:20}\n{library[key]}\n")
            time.sleep(.25)

    elif search_type == "2":
        search = input("\nEnter the Word you are looking for: ") # search for word
        for key in library.keys(): 
            if search.lower() == key.lower(): # searching for the key
                found = key.lower() 
        if found != 0: 
            print(f"\nWord:{found:6}\tDEFINITION:{library[found]}\n") # word was found
        else: 
            print(f"\nYour search for {search} came up empty :[") # word was not found
        time.sleep(2)

    elif search_type == "3":
        # Initialize the dictionary
        dictionary = {
            "python" : "a popular programming language created by Guido van Rossum",
    "documentation" : "programming comments; notes within code which explain what the code does"
    }
        add_word = input("Enter the word you wish to add: ") # adding a new word to the dictionary
        add_def = input("Enter the definition: ") # adding a definition to the new word
        library.update({f"{add_word}": f"{add_def}"}) # update library with new word and definition
        print(library.update) # display new library with newly added word and definition
        time.sleep(1)

    # exit choice from menu 
    elif search_type == "4":
        answer = "n" # exit the loop
        print("\nThank you for using the program!\n")