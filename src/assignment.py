#! /usr/bin/env python

import sys
if len(sys.argv) != 2:
    print(f"#usage {sys.argv[0]} [name]")
    sys.exit()
name = sys.argv[1]
print(name)

base = input("please write one base: ")
base = base.upper()
if base == "A":
    print("Adenine")
elif base == "C":
    print("Cytosine")
elif base == "G":
    print("Guanine")
elif base == "T":
    print("Thymine")
elif base == "U":
    print("Uracil")

try:
    num = int(input("please write number: "))
    print(10 / num)
except ZeroDivisionError as err:
    print(err)
except ValueError as err2:
    print(err2)



