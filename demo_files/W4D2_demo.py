# W4D2 in class demo search review and writing to files

# Program Promt: In the W4D2 demo, we will review utilizing sequential search for simple singular and multi returns. We will then create and write data to a text file using Python.

#--Imports----------------------------------------
import csv

#--Functions--------------------------------------

#--Main Executing Code----------------------------

#create empty lists - one for each field
dragons =[] # rec[0]
riders = [] # rec[1]
count = [] # rec[2]
color1 = [] # rec[3]
color2 = [] # rec[4]


# opens the text file
with open ("text_files/dragons.csv") as csvfile:
    file = csv.reader(csvfile)


    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        count.append(rec[2])
        color1.append(rec[3])
        
        if rec[2] == "2":
            color2.append(rec[4])
        elif rec[2] == "1":
            color2.append("---")
        else:
            color2.append("ERROR")
    #--disconected from file-----------------------------

print(f"{'DRAGONS':15} {'RIDERS':30} {'#':3} {'COLOR1':8} {'COLOR2':8}")
print("-------------------------------------------------------------------")

# process the list to dsplay data to the console
for i in range(0, len(dragons)):
    print(f"{dragons[i]:15} {riders[i]:30} {count[i]:3} {color1[i]:8} {color2[i]:8}")
print("-------------------------------------------------------------------")

# search for a specific dragon
found ="x"
search = input("Which dragon are you looking for: ")

# step 2 perform search
for i in range(0, len(dragons)):
    if search.lower() == dragons[i].lower():
        # hold onto found location of our searched-for- value
        found = i

#step 3: filter and display results
if found != "x":#search was found
    print(f"Your search for {search} was FOUND!")
    print(f"{dragons[found]:15} {riders[found]:30} {count[found]:3} {color1[found]:8} {color2[found]:8}")
else:
    print(f"Your search for {search} was  NOT FOUND!")



#search for a color set
found = []
search = input("Enter in thr dragon color you are looking for: ")

for i in range(0, len(color1)):

    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append[i]

if not found: # 'if the found list is empty
    print(f"Your search for {search} was FOUND!")
else:
    print(f"Your search for {search} was  NOT FOUND!")
    for i in range(0, len(found)):
        print(f"{dragons[found[i]]:15} {riders[found[i]]:30} {count[found[i]]:3} {color1[found[i]]:8} {color2[found[i]]:8}")

#write some data to a new file
# create a place holder name for the file
file = open('text_files/test.csv' , 'w') # create a pathway using folder name / then file name . csv 

for i in range(0, len(dragons)):
    file.write(f"{dragons[i]},{riders[i]}")

file.close()