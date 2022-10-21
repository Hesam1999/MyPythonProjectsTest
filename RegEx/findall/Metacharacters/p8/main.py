#!/usr/bin/python3

import re 

txt = "hello planet"

#Search for a sequense that starts with "he", followed by 0 or 1 (any) characters, and an "o':

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, becuase there were not zero, not one, but two characters between "he" and the "o"
