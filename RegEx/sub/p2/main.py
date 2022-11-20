#!/usr/bin/python3

import re

#Replace the first two occurrences of a white-space character whth the digit "9":

txt = "The rain in Spain"

x = re.sub("\s", "9", txt, 2)

print(x)

