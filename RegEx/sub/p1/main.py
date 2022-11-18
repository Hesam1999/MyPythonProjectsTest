#!/usr/bin/python3

import re

#Replace all white-space character whth the digit "9":

txt = "The rain in Spain"

x = re.sub("\s", "9", txt)

print(x)

