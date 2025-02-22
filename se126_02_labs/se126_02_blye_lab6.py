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
import os

#----functions-------------------------------

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


#--initalize---------------------------------------

#--create empty lists------------------------------

rowNum =[]
seatA = []
seatB = []
seatC = []
seatD = []

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