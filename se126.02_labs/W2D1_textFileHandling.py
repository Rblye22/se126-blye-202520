#W2D1 - Text File Handling - introduction

# Step 1: import the csv (comma seperated value) libary
import csv

total_records = 0 #the total number of recors (rows) in the file

#step 2
#connecting to the files path - switch \ to /
#copy relative path of file being imported

print(f"\n{'NAME':10} \t {'NUM':3} \t {'COLOR'}")
#HEADER PRINT
print("-----------------------------------")

with open("text_files/simple.csv") as csvfile:
    #indent 1 level! (new block)

    #allow processor to read the file data
    file = csv.reader(csvfile)

    #loop through every record(row) in the file
    for record in file:

        #add +1 to total_records
        total_records += 1

        print(record) #this is the list view of each record (row)

        name = record [0]
        number = record[1]
        color = record [2]

        print(f"{name:10} \t {number:3} \t {color}")
#-----------disconnected from file-------------
print(f"\n TOTAL RECORDS: {total_records}\n")