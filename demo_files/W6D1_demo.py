# W6D1 in class demo search Algorithems: Binaryy vs Sequential


#--Imports----------------------------------------
import csv

#--Functions--------------------------------------

#--Main Executing Code----------------------------

libary_nums = []
titles = []
authors = []
genres = []
pages = []


with open ("text_files/library_books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists
        libary_nums.append(rec[0])
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pages.append(rec[4])

print(f"{'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':20} {'PAGES':5}")
print("-------------------------------------------------------------------------")
for i in range(0, len(libary_nums)):
    print(f"{libary_nums[i]:5} {titles[i]:25} {authors[i]:15} {genres[i]:20} {pages[i]:5}")
print("-------------------------------------------------------------------------")

#sequential search: allow user to search for a titile
# titles[] is not ordered

found = []
search_num = input("Which Libary Num. are you looking for? ")
seq_count = 0 

for i in range(0, len(libary_nums)):
    seq_count += 1
    if search_num in libary_nums[i]: # in instead of means if something is inside of something will find search word in file is not a 1 for 1 search
        found.append(i)
print(f"SEARCH ITERATIONS: {seq_count}")

if not found:
    #lists is still empty, meaning no matches to our search term was found
    print(f"Sorry, your search for {search_num} was not found :[")

else:
    print(f"Your search for {search_num} was found :]")

    print(f"{'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':20} {'PAGES':5}")
    print("-------------------------------------------------------------------------")

for i in range(0, len(found)):
    print(f"{libary_nums[found[i]]:5} {titles[found[i]]:25} {authors[found[i]]:015} {genres[found[i]]:20} {pages[found[i]]:5}")
    print("-------------------------------------------------------------------------")


# Binary Search: must be performed on ORDERED lists (libary_nums)

min = 0
max = len(libary_nums) - 1
mid = int((min + max) /2)

bin_count = 0

while min < max and search_num != libary_nums[mid]:
    # min < max --> list has not been exhausted of potential values yet
    # search_num !+ libary_nums[mid] --> what we are looking for is not in the mid position

    if search_num < libary_nums[mid]:
        # everything after mid point is not possible 
        max = mid - 1

    else:
        #everything befor mid point is not possible
        min = mid +1

    mid = int((min - max) / 2) # can cause infinate loop if missing this line
    bin_count +=1

print(f"BINARY SARCH ITERATIONS: {bin_count}")

if search_num == libary_nums[mid]:

    print(f"Your search for {search_num} was found :]")
    print(f"{'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':20} {'PAGES':5}")
    print("-------------------------------------------------------------------------")

    print(f"{libary_nums[mid]:5} {titles[mid]:25} {authors[mid]:015} {genres[mid]:20} {pages[mid]:5}")
    print("-------------------------------------------------------------------------")

else:
    print(f"Sorry, your search for {search_num} was not found :[")