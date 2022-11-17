#!/usr/bin/python3

import re

txt = "8 times before 11:45 AM"

#Check if "Portugal" is in the  string:

x = re.findall("Portugal", txt)

print(x)

if x :
    print("Yes, there is at least one match!")
else:
    print("No match")
