#!/usr/bin/python3

# The try block will generate a NameError, because x is not defined:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Somthing else went wrong")

