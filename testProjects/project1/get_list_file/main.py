#!/usr/bin/python3

import glob

# start

path = input("path search : ")

for x in glob.iglob(path, recursive=True):
    print(x)