#W6D2 - Bubble Sorting & Binary Search Review

#https://www.google.com/search?q=bubble+sort+visualization&rlz=1C1GCHA_enUS1119US1119&oq=bubble+sort+visualization&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIICAQQABgWGB4yCAgFEAAYFhgeMg0IBhAAGIYDGIAEGIoFMg0IBxAAGIYDGIAEGIoFMg0ICBAAGIYDGIAEGIoF0gEIMzUwMmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:7e94f359,vid:0BkoXZBbhfU,st:0 

#***IMPORTANT: 
#   In order to use binary search, 2 caveats must be fulfilled:
#      *the list we intend to search through is ORDERED
#      *the list we intend to search through is populated with UNIQUE VALUES (no repeats!)

#----IMPORTS-------------------------------------------------

import csv

#----FUNCTIONS-----------------------------------------------

def display(x, foundList, records):
    '''
        PARAMETERS:
            x   signifier for if we are printing a single record or multiple when x != "x" it is an index and we have one value, otherwise we have multiple

            records   the lenght of a list we are going to process through (# of lopps/ prints)
    '''
    print(f"{'CLASS':8} {'NAME':10} {'MEANING':20} {'CULTURE'}")
    print("-----------------------------------------------------------------")
    if x !="x":
        # printing one record
        print(f"{class_type[x]:8} {name[x]:10} {meaning[x]:20} {culture[x]}")

    elif foundList:
        for i in range(0,records):
            print(f"{class_type[foundList[i]]:8} {name[foundList[i]]:10} {meaning[foundList[i]]:20} {culture[foundList[i]]}")

    else:
        # printing multiples, based on lenght stored in records
        for i in range(0, records):
            print(f"{class_type[i]:8} {name[i]:10} {meaning[i]:20} {culture[i]}")


    #print(f"{practice}")


def swap(i, listName):
    temp = name[index]
    name[index] = name[index + 1]
    name[index + 1] = temp


#----MAIN CODE-----------------------------------------------



class_type = [] #rec[0] in file; repeats --> SEQUENTIAL
name = []       #rec[1] in file; unique  --> BINARY
meaning = []    #rec[2] in file; unique  --> BINARY
culture = []    #rec[3] in file; repeats --> SEQUENTIAL

#practice = ["Austin", "Cory", "Noah", "Duncan", "Justyn"] # can also make a vertical list with a , after each name

with open("text_files/party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: 
        print(rec)
        #rec is a 1D list and file is a 2D list
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])

#disconnect from file-----------------------------------
print("-----------------------------------------------------------------")
# display whole
display("x",0,len(class_type)) # practice with function

ans = input("would you like to enter the search program? [y/n]").lower()

while ans != "y" and ans != "n":
    print("****INVALID ENTRY!****")
    ans = input("Would you like to enter the search program? [y/n]").lower()

while ans == "y":
    print("\tMENU")
    print("\t1. Search by TYPE")
    print("\t2. Search by NAME")
    print("\t3. Search by MEANING")
    print("\t4. to EXIT")

    search_type = int(input("\nHow would you like to search today? [1-4]"))


    if search_type not in ["1", "2", "3", "4"]:
        print("****INVALID ENTERY!****\nPLEASE TRY AGAIN")

    elif search_type =="1":
        print(f"\nYou have chosen to search by TYPE")

        search = input("Which type: 'dragon' or 'elf' :").lower()

        if search not in ["dragon", "elf"]:
            #could also be: if search.title() not in class_type:
            print("****INVALID ENTERY!****\nPLEASE TRY AGAIN")

        else:
            found = []
            for i in range(0, len(class_type)):
                if search.lower() == class_type[i].lower():
                    found.append(i)

            if not found:
                print(f"Sorry, your search for {search} could not be completed :[")
            
            else:
                print(f"Your search for {search} is complete! Details below:")
                display("x", found, len(found))


#BUBBLE SORT----------------------------------------

        for i in range(0, len(name) - 1):#outter loop
            # print("OUTER LOOP! i = ", i)

            for index in range(0, len(name) - 1):#inner loop
                # print("\t INNER LOOP! k = ", index)
                # below if statement determines the sort
                # list used is the list being sorted
                # > is for increasing order, < for decreasing
                if(name[index] > name[index + 1]): # < flips to order from high to low
                # print("\t\t SWAP! ", name[index], "<-->", name[index + 1])

                    # if above is true, swap places!
                    # temp = name[index]
                    # name[index] = name[index + 1]
                    # name[index + 1] = temp
                    swap(index, name)
                    
                    # swap all other values
                    swap(index, class_type)
                    swap(index, meaning)
                    swap(index, culture)

        # check your sorting
        display("x",0, len(name))

        # Binary Search
        search = input("Enter the NAME you are looking for: ")

        min = 0
        max = len(name) - 1
        mid = int((min + max) /2)


        while min < max and search != name[mid]:
            if search < name[mid]:
                max = mid -1

            else:
                #search > name[mid]
                min = mid + 1

            mid = int((min + max) /2)

        if search == name[mid]:
            display("x", 0, len(name))
        else:
            print(f"your search for {search} came up empty :[")