# Robert Blye
# SE126.02
# Lab 4
# 1-28-25

# PROGRAM PROMPT: Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension. When you are complete, display the following data for each employee (first name, last name, department, email, and phone extension) to the user. Use the following field width guide to avoid unaligned field displays:Once you have completed populating all eight parallel lists and displaying the five required back to the user (and in the same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. note: each employee’s data should be on its own record (row) within the newly created file. You will most likely end up with an extra empty line at the end of the file (this is okay for this lab as we will not be reprocessing the data found in this new file). Once the file is ready, close it and alert the user via a displayed message. Also tell them how many employees are in the file, and the total count of employees for each department. 

# print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")

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
       
    #--disconected from file-----------------------------