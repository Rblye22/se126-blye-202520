# Robert Blye
# SE126.02
# Final 
# 3/1/2025

# PROGRAM PROMPT: The program must either utilize a file or create an edited file. The program must include at minimum the use of at least two 1D lists or one 2D list. The program must showcase an understanding of control flow structures: repetition and single-decision. The program must showcase an understanding of self-built functions, to include the need for parameters as well as return values. The program must include the use of a searching algorithm: either sequential or binary (or both). The program must import at least one python library documentation include a brief program description at the start of the file include internal documentation related to the functionality of your program code documentation for anything used not introduced in the course.

# VARIABLE DICTIONARY:
# callsign = A call sign is a unique identifier used in radio communication to distinguish one station or operator from another.
# unit = The Unit of the call sign (ex. 2-70 is 2nd battalion 70th armored regigement)
# radio_freq = the frequency that the unit is on for their communications
# unit_type = type of unit they are (ex. Infantry or Tank)

#----imports-----------------------------------------------------------------------
import time
import csv

#--create csv file-------------------------------------------------------------------
callsign = ["ArchAngel", "Bayonet", "Choas", "Demon", "Shadow", "Thunder Actual"] # unit call sign
unit = ["2-70", "1-18", "1-63", "1-7", "5-4", "2-70"] # unit
radio_freq = ["138.00", "139.00", "140.00", "141.00", "142.00", "143.00"] # radio frequency
unit_type = ["Infantry", "Infantry", "Tank", "Artillery", "Scout", "Battalion-HQ"] # type of unit

#--create a csv file---------------------------------------------------------
file = open("text_files/radio_check.csv", "w") # create text file 

for i in range(0, len(callsign)):
    if i == len(callsign) -1:
        file.write(f"{callsign[i]},{unit[i]},{radio_freq[i]},{unit_type[i]}")
    else:
        file.write(f"{callsign[i]},{unit[i]},{radio_freq[i]},{unit_type[i]}\n")
file.close() # close the file

#--print header-----------------------------------------------------------------
print(f"\n{'CALLSIGN':15}\t{'UNIT':4}\t{'RADIO FREQ':10}\t{'UNIT TYPE'}")
print("-" * 70)
#--print data from the lists----------------------------------------------------
for i in range(len(callsign)):
    print(f"{callsign[i]:15}\t{unit[i]:4}\t{radio_freq[i]:10}\t{unit_type[i]}")
    time.sleep(.5)
print("-" * 70)