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

#print(f"\n{'TYPE'}\t {'BRAND'}\t     {'CPU'}\t {'RAM'}\t   {'DISK'}    {'No HDD'}\t {'2ND Disk'}    {'OS'}\t\t{'YR'}")
#HEADER PRINT


type = []
brand = []
cpu = []
ram =  []
one_disk = []
no_hdd = []
disk2 = []
os = []
year = []
d = 0
l = 0
d_mon = +2000
l_mon = +1500

with open("text_files/filehandling.csv") as csvfile:
    #indent 1 level! (new block)

    #allow processor to read the file data
    file = csv.reader(csvfile)

    #loop through every record(row) in the file
    for rec in file:

        #add +1 to total_records
        total_records += 1

        type.append(rec[0])
        brand.append(rec[1])
        cpu.append(rec[2])
        ram.append(int(rec[3]))
        one_disk.append(rec[4])
        no_hdd.append(int(rec[5]))

        if no_hdd == 1: # if it doesnt have a second drive
            disk2.append (" ")
            os.append(rec[6])
            year.append(int(rec[7]))

            #print(f"{type:10} {brand:10} {cpu:10} {ram:10} {one_disk:10}\t {no_hdd:10}\t {os:10}\t {year:10}")
            #print(f"{type:10} {brand:10} {cpu:10} {ram:10} {one_disk:10} {no_hdd:10} {disk2:10} {os:10} {year:10}")
        if no_hdd == 2: # if it has a second drive
            disk2.append(rec[6])
            os.append(rec[7])
            year.append(int(rec[8]))

            #print(f"{type:10} {brand:10} {cpu:10} {ram:10} {one_disk:10} {no_hdd:10} {disk2:10} {os:10} {year:10}")
#Disconnect from CSV FILE- ALL DATA is stored now in our lists.




for index in range (0, len(year)): #len() --> length of collection, returns # of items
    #index --> key of the list, allows acess to ONE specific value
    if year <= 16:
        
        if type == "D":
            d = d_mon + 1
            print(f"$2,000")
            
        if type == "L":
            l = l_mon
            print(f"$ 1,500")

        print(f"INDEX {index:3} : {type[index]:10} {brand[index]:10}  {cpu[index]:10}  {ram[index]:10}  {one_disk[index]:10}  {no_hdd[index]:10} {disk2[index]:10} {os[index]:10} {year[index]:10}")



 # format wont line up how i want it to. i tried \t and tried tweeking the numbers and cant seem to figure it out. the short line still stays shorter than the longer line

#-----------disconnected from file-------------
#print(f"\n TOTAL RECORDS: {total_records}\n")