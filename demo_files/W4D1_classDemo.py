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


# Write a program that allows users repeaded searches

print("\n\n Welcome to the Student Search Program\n\n")

answer = input("would you like to begin searching? [y/n]: ").lower()

while answer == "y":

    #get search type from user
    print("\tSearch Menu Options")
    print("1. Search by LAST NAME")
    print("2. Search by LETTER GRADE")
    print("3. Exit")

    search_type = input("Enter your search type [1-3]: ")

    if search_type == "1":
        print("SEARCH BY LAST NAME")
        
        found = -1 #invalid index, will check later to see if a student has been found

        #get search item from user
        search_name = input("Enter the LAST NAME of the student you are searching for: ")

        #perform search
        for i in range(0, len(lName)):
            # the for loop allows "sequence" party -> to being to end
            if search_name.lower() == lName[i].lower():  # .lower() still works
                #theIF STATEMNEt allows for "search" part
                found = i # make found the current index, can be used later to display

        #display the results
        if found!= -1:
            #last name has been found and display data
            #print(f"{fName[i]:10}   {lName[i]:10}   {test1[i]:3}   {test2[i]:3}   {test3[i]:3}   {num_avg[i]:3} {let_avg[i]}") i = 20 and will give out of range
            print(f"Your search for {search_name} was Found")
            print(f"{fName[found]:10}   {lName[found]:10}   {test1[found]:3}   {test2[found]:3}   {test3[found]:3}   {num_avg[found]:3} {let_avg[found]}")
        else:
            print(f"Your search for {search_name} was *NOT* FOUND!")
            print(f"THIS is a cAsE sensative program - check your spelling and try again!")
        
        
    elif search_type == "2":
        print("\tSearch by LETTER GRADE")
        found = [] #created empty list to gather and store index values

        #get search item from user
        search_grade = input("Enter the LAST NAME of the student you are searching for: ")

        #perform search
        for i in range(0, len(let_avg)):
            # the for loop allows "sequence" party -> to being to end
            if search_grade.upper() == let_avg[i]:
                #theIF STATEMNEt allows for "search" part
                found.append() # make found the current index, can be used later to display

        #display the results
        if not found: # this means list is empty
            print(f"Your search for {search_name} was *NOT* FOUND!")
            print(f"THIS is a cAsE sensative program - check your spelling and try again!")

        else:
            print(f"Your search for {search_name} was Found")

            #found is a list with mult. pieces of dtat - must use a for loop to see all
            for i in range(0, len(found)):
                
                print(f"{fName[found[i]]:10}   {lName[found[i]]:10}   {test1[found[i]]:3}   {test2[found[i]]:3}   {test3[found[i]]:3}   {num_avg[found[i]]:3} {let_avg[found[i]]}")

    elif search_type == "3":
        print("EXIT")
    else:...

    if search_type =="1" or search_type =="2": # only user doesnt specify 3 to exit
        answer = input("would you like to search again? [y/n]: ").lower()