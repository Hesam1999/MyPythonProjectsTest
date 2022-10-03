#!/usr/bin/python3

import json

# a Paython object (dict)
x ={
    "name":"John", 
    "age":29, 
    "city":"New York"
}

# convert into JSON
y = json.dumps(x)

# the result is a JSON string:
print(y)
