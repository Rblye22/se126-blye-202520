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
print("-------------------------------------------------------------------------------------------------------")
#header print

type = []
brand = []
cpu = []
ram =  []
one_disk = []
no_hdd = []
disk2 = []
os = []
year = []
desk = 0
lap = 0
com_total = 0

with open("text_files/filehandling.csv") as csvfile:
  
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
            year.append(rec[7])

        elif no_hdd == 2: # if it has a second drive
            disk2.append(rec[6])
            os.append(rec[7])
            year.append(rec[8])



    for index in range(0, len(type)):
        #index for computer types
    
        if year[index] <= "16": 

            if type[index] == "D": 
                desk += 1
                
            elif type[index] == "L": 
                lap += 1

            print(f"{type[index]} {brand[index]} {cpu[index]} {ram[index]} {one_disk[index]} {no_hdd[index]} {disk2[index]} {os[index]} {year[index]}")
        
d_total = desk * 2000
l_total = lap * 1500
com_total = d_total + l_total
#-----------disconnected from file-------------
print("\nBelow is the price it will cost to replace all systems that are made before 2016:\n")
print(f"To replace {desk} desktops it will cost ${d_total}")
print(f"To replace {lap} laptops it will cost ${l_total}")
print(f"It will cost of total of ${com_total} to replace all systems.")

print("\n\tPress Enter To Continue...\n")


