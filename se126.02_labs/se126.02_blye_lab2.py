# Robert Blye
# SE126.02
# Lab 2
# 1-14-2025 [W2D2]

# PROGRAM PROMPT: 
# the program is to display the amount of rooms that are over capacity and display the amount of people it is over by.


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

#--------------Imports------------------
import csv

total_records = 0 #the total number of recors (rows) in the file

print(f"\n{'TYPE':10} \t {'BRAND':3} \t {'CPU'} \t {'RAM'} \t {'DISK'} \t {'No HDD'} \t {'2ND Disk'} \t {'OS'} \t {'YR'}")
#HEADER PRINT
print("-----------------------------------")

with open("") as csvfile:
    #indent 1 level! (new block)

    #allow processor to read the file data
    file = csv.reader(csvfile)

    #loop through every record(row) in the file
    for record in file:

        #add +1 to total_records
        total_records += 1

        print(record) #this is the list view of each record (row)

        type = record [0]
        brand = record[1]
        cpu = record [2]
        ram =  record [3]
        one_disk = record [4]
        no_hdd = record [5]
        sec_disk = record [6]
        os = record [7]
        year = record [8]

        print(f"{type:10} \t {brand:3} \t {cpu:3} \t {ram:3} \t {one_disk:3} \t {no_hdd:3} \t {sec_disk:3} \t {os:3} \t {year:3}")
#-----------disconnected from file-------------
print(f"\n TOTAL RECORDS: {total_records}\n")
