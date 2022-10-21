#!/usr/bin/python3

import re

txt = "The rain in Spain"

#Check if the "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x :
    print("Yes, there is a match!")
else:
    print("No match")
