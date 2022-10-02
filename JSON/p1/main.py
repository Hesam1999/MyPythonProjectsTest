#!/usr/bin/python3

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the resault is a Python dictionary:
print(y["age"])
