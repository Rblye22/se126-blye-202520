# Robert Blye
# SE126.02
# Lab 4
# 1-28-25

# PROGRAM PROMPT: Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension. When you are complete, display the following data for each employee (first name, last name, department, email, and phone extension) to the user. Use the following field width guide to avoid unaligned field displays:Once you have completed populating all eight parallel lists and displaying the five required back to the user (and in the same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. note: each employee’s data should be on its own record (row) within the newly created file. You will most likely end up with an extra empty line at the end of the file (this is okay for this lab as we will not be reprocessing the data found in this new file). Once the file is ready, close it and alert the user via a displayed message. Also tell them how many employees are in the file, and the total count of employees for each department. 

# use this display to print - print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")

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
# 
# 
# 
# 
# 

#----imports-------------------------------

import csv

#--Initalize for function------------------

#----Functions-----------------------------


#--Main Executing Code----------------------------

#create empty lists - one for each field
fName = []
lName = []
age = []
scrnName =[]
house = []


# opens the text file
with open ("text_files/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(int(rec[2]))
        scrnName.append(int(rec[3]))
        house.append(int(rec[4]))
    #--disconected from file-----------------------------

#--EMAIL ADDRESS-----------------------------------------
email_add = scrnName + "@westeros.net"


#--DEPARTMEMT--------------------------------------------
# HOUSE STARK = Research and Development
# HOUSE TARGARYEN = Marketing
# HOUSE TULLY = Human Resources
# HOUSE LANNISTER = Accounting
# HOUSE BARATHEON = Sales
# THE NIGHT WATCH = Auditing

#--EXTENSIONS---------------------------------------------

# HOUSE STARK = ext range 100 - 199
# HOUSE TARGARYEN = ext range 200 - 299
# HOUSE TULLY = ext range 300 - 399
# HOUSE LANNISTER = ext range 400 - 499
# HOUSE BARATHEON = ext range 500 - 599
# THE NIGHT WATCH = ext range 600 - 699