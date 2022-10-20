#!/usr/bin/python3

import re 

txt = "hello planet"

#Check if the string end with 'planet':

x = re.findall("planet$", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print ("No match")
