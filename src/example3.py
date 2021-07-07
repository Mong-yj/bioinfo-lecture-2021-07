#! /usr/bin/env python

# fasta
d_base = {}
with open("059.fasta", "r") as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for i in line.strip():
            if i not in d_base:
                d_base[i] = 0
            d_base[i] += 1
print(d_base)

# fastq
with open("061.fastq", "r") as handle:
    data = handle.readlines()
count_lead = 0
count_base = 0
for i in range(1, len(data), 4):
    count_lead += 1
    count_base += len(data[i].strip())
print(count_lead)
print(count_base)

# fastq by han
cnt = 0
d_base = {}
with open("061.fastq", "r") as handle:
    for line in handle:
        if cnt % 4 == 0:  # header
            pass
        elif cnt % 4 == 1:  # base
            for i in line.strip():
                if i not in d_base:
                    d_base[i] = 0
                d_base[i] += 1
        elif cnt % 4 == 2:  # delimiter
            pass
        elif cnt % 4 == 3:  # qual
            pass
        cnt += 1
print(cnt / 4)
print(d_base)

# bed
intersum = 0
with open("077.bed", "r") as handle:
    for line in handle:
        sep_line = line.strip().split("\t")
        intersum += int(sep_line[2]) - int(sep_line[1])
print(intersum)

# bed by han
result = 0
with open("077.bed", "r") as handle:
    for line in handle:
        data = line.strip().split("\t")
        chrom, start, end = data
        length = int(end) - int(start)
        result += length
print(result)

# vcf
cnt = 0
cnt_pass = 0
with open("070.vcf", "r") as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            l_header = line.strip().split("\t")
            filter_index = l_header.index("FILTER")
            ID_index = l_header.index("ID")
            # for h in range(len(l_header)):
            #     if l_header[h] == "FILTER":
            #         filter_index = h
            #     elif l_header[h] == "ID":
            #         ID_index = h
        else:
            cnt += 1
            l_variance = line.strip().split("\t")
            if l_variance[filter_index] == "PASS":
                cnt_pass += 1
            elif l_variance[ID_index].startswith("rs"):
                print(l_variance)
print(cnt)
print(cnt_pass)

# 재귀
def fibonacci(n):
    l_fib = [0, 1]
    for i in range(2, n + 1):
        l_fib.append(l_fib[i - 1] + l_fib[i - 2])
    print(l_fib[-1])
    return l_fib


print(fibonacci(10))


def fib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))


def fib2(l, n):
    for i in range(n - 1):
        l.append(l[-1] + l[-2])
    return l


l = [0, 1]
print(fib2(l, 10))

# k-mer generation
def k_mer(l1, l2, n):
    if n < 2:
        return l2
    else:
        ltmp = []
        for s1 in l1:
            for s2 in l2:
                ltmp.append(s1 + s2)
        return k_mer(l1, ltmp, n - 1)


l1 = ["A", "T", "G", "C"]
l2 = ["A", "T", "G", "C"]
print(k_mer(l1, l2, 3))

# dictionary sort
d = {}
with open("data.txt", "r") as fr:
    for line in fr:
        l = line.strip().split(",")
        gene, val = l[0], l[1]
        d[gene] = val

print(sorted(d.items(), key=lambda x: x[0], reverse=False))
print(sorted(d.items(), key=lambda x: x[1], reverse=True))
