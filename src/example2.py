#! /usr/bin/env python
'''
# gzip 파일 읽기 by me
import gzip
base = ""
with gzip.open("covid19.fasta.gz",'rb') as f: # binary mode로 읽음
    for line in f:
        if line.decode('utf-8').startswith(">"):
            continue
        else:
            base += line.decode('utf-8').strip()
d_result = {}
for b in base:
    if b not in d_result:
        d_result[b] = 0
    d_result[b] += 1
print(d_result)

# 파일 읽기 
file_name = "covid19.fasta"
data = {}
with open(file_name,'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] += 1
print(data)

# gzip by 강사님
import gzip
file_name = "covid19.fasta.gz"

data = {}
with gzip.open(file_name, "rt") as handle: #text mode로 읽음
    for line in handle:
        if line.startswith(">"):
            continue
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] += 1
print(data)
'''
# Biopython
import gzip
from Bio import SeqIO

f = "covid19.fasta"
record = SeqIO.read(f, "fasta")
print(f"A: {record.seq.count('A')}")
print(f"C: {record.seq.count('C')}")
print(f"G: {record.seq.count('G')}")
print(f"T: {record.seq.count('T')}")

f_gz = "covid19.fasta.gz"
with gzip.open(f_gz,"rt") as handle:
    record = SeqIO.read(handle, "fasta")

print(f"A: {record.seq.count('A')}")
print(f"C: {record.seq.count('C')}")
print(f"G: {record.seq.count('G')}")
print(f"T: {record.seq.count('T')}")
'''
# 25. string
Seq1 = "ATGTTATAG"
for i in range(0,len(Seq1),3):
    print(Seq1[i])
# 26. string
for i in range(0,len(Seq1),3):
    print(Seq1[i:i+3])
# 27. string
print(Seq1[::-1])
# 28. string
d_base = {'A':'T','G':'C','C':'G','T':'A'}
comp_seq = ""
for i in Seq1:
    comp_seq += d_base[i]
print(comp_seq)

Seq1 = Seq1.lower()
Seq1 = Seq1.replace('a','T')
Seq1 = Seq1.replace('t','A')
Seq1 = Seq1.replace('c','G')
Seq1 = Seq1.replace('g','C')
print(Seq1)

#29. string
Seq1 = "ATGTTATAG"
if "C" in Seq1:
    print("Seq1 have 'C'.")
else:
    print("Seq1 have not 'C'.")
#30. string index
Seq1 = "AGTTTATAG"
for i in range(len(Seq1)-2):
    if Seq1[i:i+2] == 'TT':
        print(i)
#31. string split
seq = "AA,AC,AG,AT"
l_seq = seq.split(',')
print(l_seq)
#32.
l_seq.append("CA")
print(l_seq)
#33.
print(l_seq[::-1])

#34.
l_value = [3,1,1,2,0,0,2,3,3]
print(max(l_value))
print(min(l_value))
d_value = {}
for i in l_value:
    if i not in d_value:
        d_value[i] = 0
    d_value[i] += 1
print(d_value)
'''
