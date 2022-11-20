#!/usr/bin/python3

import re

# Search for an upper case "5" character in the begining of a word, and print its position:

txt = "The rain in Spain"

x = re.search(r"\bS\w+", txt)

print(x.span())
print(len(txt))

