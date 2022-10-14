#!/usr/bin/python3

import re 

txt = "The will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)
