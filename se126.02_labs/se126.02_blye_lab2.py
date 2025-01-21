# Robert Blye
# SE126.02
# Lab 2
# 1-18-2025 [W2D2]

# PROGRAM PROMPT: 
# the program is to display the information from the text file and organize the information about the computers in the list. If the computer has a second hard drive then display that following information as well.


# VARIABLE DICTIONARY:
# type - type of computer
# brand - manufacturer of the computer
# cpu - type of processor
# ram - ram in gb
# disk - size of hard drive
# no_hdd - number of hard drives
# os - operating system
# disk2 - size of second hard drive
# year - the year the computer was purchased
# total-records - is the total records overall in the list 

#--------------Imports------------------
import csv

total_records = 0 #the total number of recors (rows) in the file

print(f"\n{'TYPE'}\t {'BRAND'}\t     {'CPU'}\t {'RAM'}\t   {'DISK'}    {'No HDD'}\t {'2ND Disk'}    {'OS'}\t\t{'YR'}")
#HEADER PRINT
print("-------------------------------------------------------------------------------------------------------")

with open("text_files/filehandling.csv") as csvfile:
    #indent 1 level! (new block)

    #allow processor to read the file data
    file = csv.reader(csvfile)

    #loop through every record(row) in the file
    for record in file:

        #add +1 to total_records
        total_records += 1

        type = record[0]
        brand = record[1]
        cpu = record[2]
        ram =  record[3]
        one_disk = record[4]
        no_hdd = record[5]

        if no_hdd == "1": # if it doesnt have a second drive
            disk2 = " "
            os = record[6] 
            year = record[7]

            #print(f"{type:10} {brand:10} {cpu:10} {ram:10} {one_disk:10}\t {no_hdd:10}\t {os:10}\t {year:10}")
            print(f"{type:10} {brand:10} {cpu:10} {ram:10} {one_disk:10} {no_hdd:10} {os:10} {year:10}")
        if no_hdd == "2": # if it has a second drive
            disk2 = record[6]
            os = record[7]
            year = record[8]

            print(f"{type:10} {brand:10} {cpu:10} {ram:10} {one_disk:10} {no_hdd:10} {disk2:10} {os:10} {year:10}")
 # format wont line up how i want it to. i tried \t and tried tweeking the numbers and cant seem to figure it out. the short line still stays shorter than the longer line

#-----------disconnected from file-------------
print(f"\n TOTAL RECORDS: {total_records}\n")