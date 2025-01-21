#W3D2 - List Review - 1Dimensional List & Parallel List

#this filr uses: class_grades.csv

#---------Imports------------------------
import csv

#---------Functions----------------------

#---------Main Executing Code------------

total_records = 0\

#create a list for every potenial field

firstname = []
lastname = []
test1 = []
test2 = []
test3 = []

with open ("text_files/class_grades.csv") as csvfile:

    file = csv.reader (csvfile)

    for rec in file:
        #for every record in the file do the following
        #print(f"{rec[0]:10}\t{rec[1]:10}")

        #fname = rec[0]
        #lname = rec [1]

        #add the record data to its corresponding list (1 list per field)
        #append--> to add to the end
        firstname.append(rec [0])
        lastname.append(rec[1])

        test1.append(int(rec[2])) #cast as integer for easier math later
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

# disconnect from the the file -- all file data is retained bc we are using lists

#create a new list to hold each students test scores average
avg = []

#process the current students data to find and store each student's test score avg to the avg list
for i in range(0, len(test1)):
    a = (test1 + test2 +test3) / 3
    avg.append(a)
    #could also avg.append((test1[i] + test2[i] + test3[i]) /3)

#basic procesing - use the 1D parallel lists to print all data to the console
print(f"INDEX {'#':3} : {'FIRST':10} {'LAST':10}  {'T1':3}  {'T2':3}  {'T3':3} {'AVG':3}")
print("-----------------------------------------------------------------------")

for index in range (0, len(firstname)): #len() --> length of collection, returns # of items
    #index --> key of the list, allows acess to ONE specific value

    print(f"INDEX {index:3} : {firstname[index]:10} {lastname[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3}  {avg[index]:3.2f}")
print("--------------------------------------------------------------------\n")

total_avg = 0 

#find current avg of the class by processing the avg list data
for i in range(0,len (avg)):
    total_avg += avg[i] #addes avg value to the total avg var

    #calculate the average
    class_avg = total_avg / len(avg)
    print(f"\n THE CLASS AVERAGE of these {len(avg)} students is : {class_avg:.2f}")
    #test