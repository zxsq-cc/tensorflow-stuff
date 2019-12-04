import os
import random

path = '/home/pi/Desktop/imgcap'
prepend = ['i', 'm', 'g', '0', '0', '0']

def getRand():
    field = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return field[random.randint(0,21)]

for fileName in os.listdir("."):
    if fileName.startswith("img00"):
        print(fileName)
#         for i in range(5):
#             handval = getRand()
#             prepend[i] = handval
#             handval = 'x'
#         
#         os.rename(fileName, fileName.replace("img00", prepend))