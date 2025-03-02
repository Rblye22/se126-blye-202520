# Robert Blye
# SE126.02
# Midterm pt. 2
# 2/4/2025

# PROGRAM PROMPT: Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold a “status” value for each book. Assign each book a status value of “On Loan” or “Available” and store to the newly created list. Half of the books should be “On Loan” and the other half should be “Available” – you can decide which books hold which status as long as it is an even split between the two potential values. Once the new list is populated, process through the five lists to display all of the data to the user as well as the total number of records in the file. Once all of the data has been displayed, write all of the list data to a new file called ‘midterm_choice2.csv’, where each book’s information is found on one record in the file and their data is separated by a comma (additional empty line in resulting file is okay). Finally, create a sequential search program that allows a user to repeatedly search the book database information stored in the lists based on the following menu:

# VARIABLE DICTIONARY:
# callsign = A call sign is a unique identifier used in radio communication to distinguish one station or operator from another.
# unit = The Unit of the call sign (ex. 2-70 is 2nd battalion 70th armored regigement)
# radio_freq = the frequency that the unit is on for their communications
# unit_type = type of unit they are (ex. Infantry or Tank)
# 
# 
# 
# 
# 
# 
# 
# 
# 
#


#----imports-----------------------------------------------------------------------

import time
import csv

#--create csv file-------------------------------------------------------------------

callsign = ["ArchAngel", "Bayonet", "Choas", "Demon", "Shadow", "Thunder Actual"] #
unit = ["2-70", "1-18", "1-63", "1-7", "5-4", "2-70"] #
radio_freq = ["138.00", "139.00", "140.00", "141.00", "142.00", "143.00"] 
unit_type = ["Infantry", "Infantry", "Tank", "Artitllery", "Scout", "Battalion-HQ"]

#--create a csv file---------------------------------------------------------
file = open("text_files/radio_check.csv", "w") # create text file 

for i in range(0, len(callsign)):
    file.write(f"{callsign[i]},{unit[i]},{radio_freq[i]},{unit_type[i]}\n") # data for text file \n will add them to a new line at the end
file.close() # close the file

#--initialize------------------------------------------------------------------


#--print header-----------------------------------------------------------------
print(f"\n{'CALLSIGN':15}\t{'UNIT':4}\t{'RADIO FREQ':10}\t{'UNIT TYPE'}")
print("-" * 70)

#--print data from the lists----------------------------------------------------
for i in range(len(callsign)):
    print(f"{callsign[i]:15}\t{unit[i]:4}\t{radio_freq[i]:10}\t{unit_type[i]}")
print("-" * 70)