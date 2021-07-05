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
'''
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
        
