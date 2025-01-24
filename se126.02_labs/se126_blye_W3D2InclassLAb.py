# Robert Blye
# SE126.02
# W3D2 Inclass-lab
# 1-24-25

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
# total_records - is the total records overall in the list 
# desk -  number of desktops
# lap - number of laptops
# com_total - cost to replace all computers
# d_total - cost to replace all desktops
# l_total - cost to replace all laptops
#--------------Imports------------------
import csv

total_records = 0 #the total number of recors (rows) in the file
print(f"\n{'TYPE'}\t {'BRAND'}\t     {'CPU'}\t {'RAM'}\t   {'DISK'}    {'No HDD'}\t {'2ND Disk'}    {'OS'}\t\t{'YR'}")
#HEADER PRINT
print("-------------------------------------------------------------------------------------------------------")

#-----initilizing------
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

    #loop through every record in the file
    for rec in file:

        type.append(rec[0])
        brand.append(rec[1])
        cpu.append(rec[2])
        ram.append(int(rec[3]))
        one_disk.append(rec[4])
        no_hdd.append(int(rec[5]))

        desk = 0 # desktops
        lap = 0 # laptops
        com_total = 0 # overall cost
        d_total = desk * 2000 # mult to get total cost for desktops
        l_total = lap * 1500 # mult to get total cost for laptops

        if no_hdd == 1: # if it doesnt have a second drive
            disk2.append(" ")
            os.append(rec[6])
            year.append(rec[7])

           
        elif no_hdd == 2: # if it has a second drive
            disk2.append(rec[6])
            os.append(rec[7])
            year.append(rec[8])

    for index in range(0, len(type)):
        #index for computer types
    
        if year[index] <= 16:
            com_total = d_total + l_total # total cost to replace all computers if they choose to replace both desktops and laptops

            if type[index] == "D":  # number of desks tops that need to be replaced
                desk += 1
                
            elif type[index] == "L":  # number of laptops that need to be replaced
                lap += 1

        print(f"{type[index]:10} {brand[index]:10} {cpu[index]:10} {ram[index]:10} {one_disk[index]:10} {no_hdd[index]:10} {disk2[index]:10} {os[index]:10} {year[index]:10}") # list of computers
        
d_total = desk * 2000 # cost to replace desktops made before 2016, num of desktops mult. by 2000
l_total = lap * 1500  # cost to replace laptops made before 2016, num of laptops mult by 1500

#-----------disconnected from file-------------

print("\nBelow is the price it will cost to replace all systems that are made before 2016 by type:\n") 
print(f"To replace {desk} desktops it will cost ${d_total}") # showing price to replace desktops
print(f"To replace {lap} laptops it will cost ${l_total}") # showing price to replace laptops

input("\n\tPress Enter To Continue...\n")
print(f"It will cost of total of ${com_total} to replace all systems.")


