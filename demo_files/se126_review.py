#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------
def swap(j,listName):
    temp = listName[j]
    listName[j] = listName[j + 1]
    listName[j + 1] = temp


#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)                           #entire list
print(names_list[0])                        #first value  
print(names_list[len(names_list) -1])       #last value

#create a empty list for each potental field
#theses MUST remain the same length in order to be parallel
names = [] 
riders = [] 
nums = [] 
color1 = [] 
color2 = [] 

#creation & population of dictionaries
people_dictionary ={
    #"key" : value
    "fname" : "George",
    "mname" : "Bulleit",
    "lname" : "Wayne",
    "age" : 12, # no key duplicates or it will use the last one to replace it
    "age" :12.5

}

print(people_dictionary)
print(people_dictionary["fname"])


dragon_dict = {}

#gaining data from a text file 
with open("text_files/dragons-1.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        print() #we will replace this during demo

        #adding data to a list
        names.append(rec[0]) 
        riders.append(rec[1]) 
        nums.append(rec[2]) 
        color1.append(rec[3])

        if rec[2] =="2":
            color2.append(rec[4])
        else:
            #still need to assign data to dragon color 2 to keep them parallel
            color2.append("---")
            color_var = "---"

        #adding data to a dictionary
        dragon_dict.update({rec[0] : [rec[1], rec[2], rec[3], color_var]}) 

#dictionaries --> for key in dictionary:
for key in dragon_dict:
    print(f"{key.upper():15} {dragon_dict[key]}") # this shows us the list data fouind at each key
    for value in dragon_dict[key]:
        print(f"{key} - {value}", end ="")
        print("\n")
    # different way to do the same as above
    for i in range(len(dragon_dict[key])):
        print(f"{key} / {dragon_dict[key][i]}",end = "}")
        print("\n")
print("-" * 75)

#processing data from collections
# lists --> standard for i in range()
print(f"{'NAMES':12} {'RIDERS':30} {'NUM':3} {'color1':8} {'color2'}")
print("-" * 75)
for i in range(0, len(names)):
    print(f"{names[i]:12} {riders[i]:30} {nums[i]:3} {color1[i]:8} {color2[i]}")
print("-" * 75)

#searching & sorting
#sequential search for multiple return values
search = input("\n Enter the Rider name you wish to find: ")
found = []

for key in dragon_dict:
    if search.lower() in dragon_dict[key][0]:
        found.append(key) # adds key of found location to the list

if not found:
    #found list is still empty, no search returned
    print(f"Sorry your search for {search} came up empty!\n")

else:
    print(f" Here are the results for your search of {search}: ")
    for i in range(len(found)):
        print(f"{found[i].upper():15} {dragon_dict[found[i]][0]:30} {dragon_dict[found[i]][1]} {dragon_dict[found[i]][2]:8} {dragon_dict[found[i]][3]}")


# Binary Search *requires* sorting before searching, must also ensure the collection we search through is populated with unique values

#Buble Sort algorithm - loop in a loop
for i in range(0, len(names) - 1):
    for j in range(len(names) -1):
        if names[j] > names[j +1]: # > = ascending order  0 to last < = last to 0 
            swap(j, names)
            swap(j, riders)
            swap(j, nums)
            swap(j, color1)
            swap(j, color2)


search = input("\nEnter the Dragon Name you wish to find: ")
min = 0
max = len(names) -1
mid = int((min + max) / 2)

while min < max and search.lower() != names[mid].lower(): # if == it will not show result for search
    if search.lower() < names[mid].lower():
        max = mid - 1
    else:
        min = mid + 1
    mid = int((min + max) / 2) # re-value it in the statement

if search.lower() == names[mid].lower():
    print(f"\nWe found your search for {search} in record #{mid}, see info below!\n")
    print(f"{names[mid]:12} {riders[mid]:30} {nums[mid]:3} {color1[mid]:8} {color2[mid]}\n")

else:
    print(f"Sorry we could not find your search for {search}!\n")
    
#2D lists - lists of lists
letters = [
    # 0,  #1,  #2
    ["A", "B", "C"], # 0
    ["D", "E", "F"], # 1
    ["G", "H", "I"] # 2
]

print(letters)
print(letters[0]) # "A", "B", "C"
print(letters[0][0]) # A
print(letters[0][len(letters[0]) -1 ])
print(letters[2][1]) # H
