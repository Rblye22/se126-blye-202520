#Robert Blye
#SE126.02
#in_class_lab
#1-7-2025 [W1D2]

#PROGRAM PROMPT: 
#


#VARIABLE DICTIONARY:
#
#
#
#
# 
# 
# 
# 


#--------------Imports------------------
import csv

total_records = 0 #the total number of recors (rows) in the file
#-------Header--------------------
print(f"\n{'ROOM':10} \t {'NUM':3} \t {'REG'}")
#HEADER PRINT
print("-----------------------------------")


with open("text_files/classLab2.csv") as csvfile:

     file = csv.reader(csvfile)

     for record in file:

        total_records += 1

        #print(record) #this is the list view of each record (row)

        room = record [0]
        num_ppl = int(record[1])
        ppl_reg = int(record [2])

        if ppl_reg > num_ppl:
            #num_ppl = int(num_ppl)
            #ppl_reg = int(ppl_reg)
            wait = (num_ppl - ppl_reg) * - 1

            print(f"{room:10.10} \t {num_ppl:15} \t {ppl_reg:2} \t {wait}")
        '''
        if ppl_reg > ppl_reg:
            num_ppl = int(num_ppl)
            ppl_reg = int(ppl_reg)
            wait_list = num_ppl
        '''
#-----------disconnected from file-------------
print(f"\n There were {total_records} rooms processed and {wait} are over the limit. \n")