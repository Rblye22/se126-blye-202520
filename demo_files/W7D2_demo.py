# W7D2 Binary search and bubble sort 2D lists

def menu():
    print("Simple Search Menu")
    print("1. Search by Name")
    print("2. Search by Number")
    print("3. Search by Color")
    print("4. EXIT")

    menu_choice = input(" Enter your search type [1-4]: ")
    return menu_choice

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

    
import csv

# create empty 1D parallel lists
names = []
nums = []
colors = []

valid_menu = ["1", "2", "3", "4"]

with open ("text_files\simple.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        names.append(rec[0]) 
        nums.append(rec[1]) 
        colors.append(rec[2].title())

ans = "y"

while ans == "y":
    choice = menu()

    if choice not in valid_menu:
        print("!Invalid Entery!\n Please Try Again.\n")

    elif choice == "1":
        print("~Search by Name~")

        # bubble sort befor binary:
        for i in range(len(names) -1):
            for j in range(len(names) -1):
                # see if larger value comes before smaller
                if names[j] > colors[j +1]:
                    # swap places - not just this value, but all associated values!
                    swap(j, colors)
                    swap(j, names)
                    swap(j, nums)

        min = 0 # always start value --> First index / lowest value in ascending order list
        max = len(names) - 1 # last index / highest in asending order list
        mid = int((min + max) / 2) # Middle index / middle value in ascending order list

        search = input("Enter the NAME you are looking for: ")

        while min < max and search.lower() != names[mid].lower():
            if search.lower() < names[mid].lower():
                max = mid - 1

            else:
                max = mid +1

            mid = int((min + max) / 2)
            
        if search.lower() == names[mid].lower():
            print(f" your search for {search} is complete, see below for details: ")
            print(f"{'Name':8}  {'Num:3'}   {'Color'}")
            print("-------------------------------------------------------")
            print(f"{names[mid]:8}  {nums[mid]:3}   {colors[mid]}")
            print("-------------------------------------------------------")

        else:
            print(f"your search for {search} is complete, and no information was found. ")

    elif choice == "2":
        print("~Search by Number~")

    elif choice == "3":
        print("~Search by Color~")
        # bubble sort before binary:
        for i in range(len(colors) -1):
            for j in range(len(colors) -1):
                # see if larger value comes before smaller
                if colors[j] > colors[j +1]:
                    # swap places - not just this value, but all associated values!
                    swap(j, colors)
                    swap(j, names)
                    swap(j, nums)

        min = 0 # always start value --> First index / lowest value in ascending order list
        max = len(colors) - 1 # last index / highest in asending order list
        mid = int((min + max) / 2) # Middle index / middle value in ascending order list
        
        search = input("Enter the NAME you are looking for: ")

        while min < max and search.lower() != colors[mid].lower():
            if search.lower() < colors[mid].lower():
                max = mid - 1
            else:
                max = mid +1
            mid = int((min + max) / 2)
            
        if search.lower() == colors[mid].lower():
            print(f" your search for {search} is complete, see below for details: ")
            print(f"{'Name':8}  {'Num:3'}   {'Color'}")
            print("-------------------------------------------------------")
            print(f"{names[mid]:8}  {nums[mid]:3}   {colors[mid]}")
            print("-------------------------------------------------------")
    else:
        print("\n~EXIT~")
        ans = "x" # ans changes from "y" to end the loop

print("Thank you for using the program!")

# 2D lists
dataFile = [
    names, # list of names
    nums, # list of numbers
    colors # lists of colors
]

dataFile = [] 
with open ("text_files\simple.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dataFile.append(rec)

print("\n\nDATA FILE (2D List[][]):")
for i in range(0, len(dataFile)):
    # accessing each list within 2D list dataFile
    print(f"Index {i} of 'DataFile': {dataFile[i]}")
    for j in range(0, len(dataFile[i])):
        # accessing each value within the list currently looked at from outter for loop
        print(f"Index {i} of 'DataFile': {dataFile[i][i]}")