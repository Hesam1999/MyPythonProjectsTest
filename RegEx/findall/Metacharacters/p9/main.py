#!/usr/bin/python3

import re 

txt = "hello planet"

#Search for a sequense that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)
