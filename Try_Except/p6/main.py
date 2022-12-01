#!/usr/bin/python3

# The finally block will raise an error when  trying to write to a read-only file:

try:
    f = open("/home/hesam/Documents/python_py/Try_Except/p6/demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writting to the file")
    finally:
        f.close()
except:
    print("Somthing went wrong when opening the file")

