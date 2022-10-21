#!/usr/bin/python3

import re

txt = "The rain in Spain"

#Check if "ain" is present, bot NOT at the end of a word:

x = re.findall(r"ain\B", txt)

print(x)

if x :
    print("Yes, there is at least one match!")
else:
    print("No match")
