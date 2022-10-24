#!/usr/bin/python3

import re

txt = "The rain in Spain"

#Check if the string contains any digits (number from 0-9):

x = re.findall("\d", txt)

print(x)

if x :
    print("Yes, there is at least one match!")
else:
    print("No match")
