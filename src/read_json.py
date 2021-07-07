#! /usr/bin/env python

import json

with open("test.json", "r") as handle:
    data = json.load(handle)
print(data)

for i in data:
    for j in i.values():
        print(j, end="\t")
    print()

for elem in data:
    print(f"{elem['id']}\t{elem['sequence']}\t{elem['species']}")
