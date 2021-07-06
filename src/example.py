#! /usr/bin/env python
'''
# 02. variable
import math 
import sys
r = int(sys.argv[1])
result = r*r*math.pi
print(result)
# 03. Operator
num1=3
num2=5
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1%num2)
print(num1**num2)

# 04. if-else
num1 = 3
if num1 % 2 == 0:
    print(num1, "is even number")
else:
    print(num1, "is odd number")

# 05. if-elif-else
num1 = 21
if (num1 % 3 == 0) and (num1 % 7 == 0):
    print(num1,"은 3과 7의 배수")
elif num1 % 3 == 0:
    print(num1,"은 3의 배수")
elif num1 & 7 == 0:
    print(num1,"은 7의 배수")
else:
    print(num1,"은 3과 7의 배수가 아니다")

# 06. for
summation = 1
for i in range(1,11):
    summation *= i
print(summation)

print(sum([i for i in range(1,11)]))

# 07. dup_for
for i in range(2,10,2):
    for j in range(1,10):
        print("%d * %d = %d"%(i,j,i*j))
    print("-------------------")

# 08. while
i = 1
result = 1
while i < 6:
    result *= i
    i += 1
print(result)

# 09. function
def greet():
    print("Hello, Bioinformatics")
greet()
greet()

# 10. function2
def mySum(x,y):
    return x+y

print(mySum(2,3))
print(mySum(10,15))

# 11-12. function3
def factorial(n):
    val = 1
    while n > 0:
        val *= n
        n -= 1
    return val
print(factorial(5))

# 13. input
in_value = input("write your name: ")
print(f"hello {in_value}")

# 14. input2
in_word = input("write one word: ")
if in_word.isdigit():
    print("interger")
else:               # .isalpha()
    print("string")

# 15. sys
import sys
if len(sys.argv) !=2:
    print(f"python {sys.argv[0]} [sample]")
    sys.exit(1)

arg = sys.argv[1]
print(f"Hello {arg}.")

# 16. file read
file_name = "read_sample.txt"
with open(file_name, 'r') as handle:
    for line in handle:
        print(line.strip())

handle = open("read_sample.txt",'r')
#for line in handle:
#    print(line.strip())
lines = handle.readlines()
print(lines)
for line in lines:
    print(line.strip())
handle.close()

# 17. file write
handle = open("write_sample.txt","w")
handle.write("Hello\n")
handle.write("Bioinformatics\n")
handle.close()

with open("write_sample2.txt",'w') as handle:
    handle.write("Hello\n")

s = "s1,s2,s3" #csv
data = s.split(',')
print(data)

with open("write_sample3.txt", "a") as handle:
    handle.write("\t".join(data)) #tsv

# 19. Debugging
try: 
    with open("naname.txt",'r') as fr:
        read = fr.readlines()
        print(read)
except:
    print("there are no naname.txt")

# 19-2. Debugging
import sys
try:
    num = int(sys.argv[1])
except ValueError as err:
    print(err)
    sys.exit(2)
except IndexError as err2:
    print(err2)
    sys.exit(3)
    
try:
    num = int(input("Enter: "))
    print(10/num)
except ZeroDivisionError as err:
    print(err)
    print("0으로 나눌 수 없습니다.")
except ValueError as err:
    print(err)

'''
# 20. string
a = "Bio"
b = "Informatics"
print(a+b)

# 21. string2
Seq1 = "AGTTTATAG"
print(Seq1[5])
# 22. string3
print(Seq1[3:6])
# 23.string4
print(len(Seq1))
# 24. string5
Seq1 = "ATGttATaG"
print(Seq1.upper())
print(Seq1.lower())

# class
class A:
    def __init__(self,val):
        self.val = val
    def __add__(self,other):
        return self.val + other.val
    def __mul__(self,other):
        return "__mul__"
    def __len__(self):
        return 0

a1 = A(1)
a2 = A(2)
print(a1.val + a2.val)
print(a1+a2) #__add__
print(a1*a2) #__mul__
print(len(a1))

