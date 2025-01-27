#W4D1 - sequentail search

#PROGRAM PROMT: we will continue to work with class_grades.csv file as in the W3D2 demo. practice connecting 

#this file uses: class_grades.csv

#----imports-------------------------------
import csv

#----Functions-----------------------------

def letter(num):
    if num >= 90:
        let ="A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60: 
        let = "F"
    else:
        let = "ERROR"

    return let #'let' value replaces the func call in the main executing code

#create empty lists to hold the file data
fName = []
lName = []
test1 = []
test2 = []
test3 = []

with open ("text_files/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

# disconnected from file -- can still acess stored data via the list

# process the list data to calc an avg score for each student, and find a letter grade equivalent

num_avg = [] # holds each students num avg of test scores
let_avg = [] # holds each students let acg of test scores

for i in range(0,len(fName)):

    a = (test1[i] + test2[i] + test3[i]) / 3
    #add avg to num_avg list
    num_avg.append(a) # can also do: num_avg.append((test1[i] + test2[i] + test3[i]) /3)

    l = letter(a) #reurn value of letter() stored to i
    let_avg.append(l) # can also do : let_avg.append(letter(a))

#process the lists to diaplay all data back to the user
for i in range(0, len(fName)):
    print(f"{fName[i]:10}   {lName[i]:10}   {test1[i]:3}   {test2[i]:3}   {test3[i]:3}   {num_avg[i]:3} {let_avg[i]}")

print("-------------------------------------------------------------------------")

print(f"There are {len(fName)} Students in the file.")