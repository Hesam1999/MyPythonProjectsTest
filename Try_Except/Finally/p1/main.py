#!/usr/bin/python3

# The finally block gets executed no matter if the try block raises any errors or not:

try:
    print(x)
except:
    print("Somthing else went wrong")
finally:
    print("The 'try except' is finished")

