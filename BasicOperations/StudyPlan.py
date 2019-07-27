'''
Created on 27 de jul de 2019

@author: JPereira3
'''
from time import sleep

areas_of_studying = {1 : "AWS", 2 : "Azure", 3 : "CISSP", 4: "GIAC", 5: "EC-Council", 6: "Law School", 7: "DataScience", 8: "Programming"}

total = len(areas_of_studying)

print(total)

print()
print()

for x in areas_of_studying:
    print(areas_of_studying[x])

print()
print()

print("Calculating your social life status....")
sleep(2)
print()
print()

print("Number of Disciplines %d" %total + "....")
sleep(1)
print()
print()

print("number of working days: " + "5")
sleep(1)
print()
print()

if total > 5:
    print("You're so fucked.... Good luck mate. :p")
    

