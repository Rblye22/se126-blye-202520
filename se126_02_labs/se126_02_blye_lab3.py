# Robert Blye
# SE126.02
# Lab 3
# 1-24-25

# PROGRAM PROMPT: 
# the program is to display voter information of the number of individuals not eligible to register, number of individuals who are old enough to vote but have not registered, number of individuals who are eligible to vote but did not vote, number of individuals who did vote, and the number of records processed.


# VARIABLE DICTIONARY:
# id - id number
# age - voters age
# registered - if the voter is registered to vote or not
# vote - if the voter voted or not
# total_rec - total number of records being processed
# eligible - person is able to vote
# not_eligible - person is not able to vote
# not_reg - not registered to vote
# ppl_ reg - people registered to vote but did not vote
# voted - the number of people who voted

#--------------Imports------------------
import csv

#-----initilizing------
id = []
age = []
registered = []
vote = []

total_rec = 0
not_eligible = 0
eligible = 0
not_reg = 0
ppl_reg = 0
voted = 0
reg_vote = 0


print("print(f'ID' 'AGE' 'registered' 'vot' ")
with open("text_files/voters_202040.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

    for rec in file:

        id.append(rec[0])
        age.append(rec[1])
        registered.append(rec[2])
        vote.append(rec[3])

    for index in range(0, len(id)):

        if age[index] < "18":
            not_eligible += 1
        
        elif registered[index] == "N":
            not_reg += 1
            
        elif registered[index] =="Y" and vote[index] == "N":
            reg_vote += 1

        elif vote[index] == "Y":
            voted +=1

        total_rec += 1
            
        print(f"{id[index]:10} {age[index]:10} {registered[index]:10} {vote[index]:10}")

    #Number of individuals not eligible to register.
print(f"There are {not_eligible} people who are not eligible to vote.") 

#Number of individuals who are old enough to vote but have not registered.
print(f"There are {not_reg} people not registered to vote.")

#Number of individuals who are eligible to vote but did not vote.
print(f"There are {reg_vote} people that are eligible to vote but did not vote.")

#Number of individuals who did vote.
print(f"There was {voted} people who voted")

#Number of records processed.
print(f"There was {total_rec} processed.")