# W8D2 in class demo - Dictionaries + textfile data

#--Imports----------------------------------------------------------
import csv
#--Main Executing Code-----------------------------------------------


#--mini review on dictionaries----------------------------------------
library = {
    # indexes are strings set by the dev
    #'key' : value
    "1230" : "Red Rising",  # can make them on the same line
    "1231" : "The Little Prince"

}

with open("text_files/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        # add each record data as a new key + value pair from the text file
        # key --> rec[0] ; value --> rec[1]
        library.update({rec[0] : rec[1]})
        # when using .update() --> pass {'key' : value}

#--disconnect from file----------------------------------------------------

#--header print------------------------------------------------------------
print(f"\n{'KEY':6}\t{'TITILE'}")
print("-" * 50) # print("---------------------------------------------------")
for key in library:
    # loops runs for every key (and value) pair found within the libary dictionary
    print(f"{key:6}\t{library[key]}")
print("-" * 50)


#--Sequential search for a title------------------------------------------------
search = input("Enter the TITLE you are looking for: ")

found = 0

for key in library:
    if search.lower() == library[key].lower():
        # store the found titiles location in the dictionary -->
        found = key

if found != 0:
    print(f"\nkey:{found:6}\tTITILE:{library[found]}")
else:
    print(f"Your search for {search} came up empty!")

#--binary search for library for libarary number (dictionary keys)
# in order to binary search for a set of keys you must first copy dictionary into lists, # get it from canvas #

# type() returns the class types of the data passed to it
if type(library) is dict:
    print("'library' is a DICTIONARY")