# Robert Blye
# SE126.02
# Lab 4
# 1-31-25

# PROGRAM PROMPT: utilize the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension. When you are complete, display the following data for each employee (first name, last name, department, email, and phone extension) to the user. Once you have completed populating all eight parallel lists and displaying the five required back to the user, create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. Once the file is ready, close it and alert the user via a displayed message. Also tell them how many employees are in the file, and the total count of employees for each department. 

# VARIABLE DICTIONARY:
# clear() = clear the display terminal
# fName = employees first name
# lName = employees last name
# age = employess age
# scrnName = employees screen name
# house = employees house of allegience
# email_list = the list of employee emails
# email = employee email address
# dep = employees department
# phone_ext = employees phone extension
# ext =  used to assign random employee phone extension
# total_rec =  total number of records
# res_total = total of employees in Research & Development
# m_total = total of employees in Marketing
# h_total = total of employees in Human Resources
# acc_total = total of employees in Accounting
# s_total = total of employees in Sales
# aud_total = total of employees in Auditing
# i = index

#----imports-------------------------------

import time
import csv
import random
import os

#--functions-----------------------------------

def clear():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/MacOS
        os.system('clear')

#--Main Executing Code----------------------------

#create empty lists - one for each field
fName = []
lName = []
age = []
scrnName =[]
house = []
email_list = []
dep = []
phone_ext = []

#--initialize---------------------------------------

total_rec = 0
res_total = 0
m_total = 0
h_total = 0
acc_total = 0
s_total = 0
aud_total = 0

# opens the text file
with open ("text_files/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists

        total_rec += 1 
        # total record counter

        fName.append(rec[0]) # first name append
        lName.append(rec[1]) # last name append
        age.append(int(rec[2])) # age append
        scrnName.append(rec[3]) # screen name append
        house.append(rec[4]) # house append
        
    #--disconected from file-----------------------------

#for i in range(0, len(fName)):
    #print(f"{fName[i]:8} {lName[i]:}\t {age[i]:8}\t {scrnName[i]:2}\t\t{house[i]}") # print list

clear()

print("-------------------------------------------------------------------------------")

for i in range(len(fName)):
    # email name created
    email = scrnName[i] + "@Westeros.net"
    email_list.append(email) # append the email name to the email list

    # assign department and extension from house name

    if house[i] == "House Stark": # house
        dep.append("Research & Development") # department
        ext = random.randint(100, 199) # random int 
        res_total += 1

    elif house[i] == "House Targaryen": # house
        dep.append("Marketing") # department
        ext = random.randint(200, 299) # random int
        m_total += 1 


    elif house[i] == "House Tully": # house
        dep.append("Human Resources") # department
        ext = random.randint(300, 399) # random int
        h_total += 1

    elif house[i] == "House Lannister": # house
        dep.append("Accounting") # department
        ext = random.randint(400, 499) # random int
        acc_total += 1

    elif house[i] == "House Baratheon": # house
        dep.append("Sales") # department
        ext = random.randint(500, 599) # random int
        s_total += 1

    else:
        house[i] == "The Night’s Watch"  # house
        dep.append("Auditing") # department
        ext = random.randint(600, 699) # random int
        aud_total += 1

    # Append the extension to the phone extension list
    phone_ext.append(ext)

#--print header-----------------------------------------------------------

print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")

print("-------------------------------------------------------------------------------")

# print data from the lists
for i in range(len(fName)):
    print(f"{fName[i]:8} {lName[i]:10} {email_list[i]:30} {dep[i]:23} {phone_ext[i]:3}")

file = open('text_files/westeros.csv' , 'w') # create text file 

for i in range(0, len(fName)):
    file.write(f"{fName[i]},{lName[i]},{email_list[i]},{dep[i]},{phone_ext[i]}\n") # data for text file \n will add them to a new line at the end
file.close() # close the file

print("-------------------------------------------------------------------------------")
 
time.sleep(3) # screen sleep timer in seconds

print(f"\n\tYour file is ready!") # file has been uploaded
time.sleep(1)
print(f"\n\tThere are {total_rec} employees in the file")
time.sleep(1) # total employees 
print(f"\n\tThere are {res_total} employees in Research & Development") # total count for each department
time.sleep(1)
print(f"\n\tThere are {m_total} employees in Marketing") # total count for marketing
time.sleep(1)
print(f"\n\tThere are {h_total} employees in Human Resources") # total count for marketing
time.sleep(1)
print(f"\n\tThere are {acc_total} employees in Accounting") # total count for accounting
time.sleep(1)
print(f"\n\tThere are {s_total} employees in Sales") # total count for sales
time.sleep(1)
print(f"\n\tThere are {aud_total} employees in Auditing") # total count for auditing
time.sleep(1)
print("-------------------------------------------------------------------------------")
print("\n\tThank you for using the program!") # goodbye message