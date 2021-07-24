
# MATH FUNCTIONS


import math
def tan(x):
    return math.atan(x)
def tan2(y,x):
    return math.atan2(y,x)

print(tan(12))
print(tan2(10,20))


# FIND MAX LENGTH IN LIST
test_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',  'August', 'September', 
        'October', 'November', 'December']

max_len = 1
for ele in test_list:
    if len(ele) > max_len:
        max_len = len(ele)
        res = ele

# printing result
print("Maximum length string is : " + res)


# SUM OF ODD,EVEN OF A,B


a = "123"
b = "234"
lst = []
for i in a:
    lst.append(int(i))
for j in b: 
    lst.append(int(j))
    
print(lst)
Sum = sum(lst)
print(Sum)


# PRINT 1 - 100 USING RECURSION


def printNos(n):
    if n > 0:
        printNos(n-1)
        print(n, end = ' ')
 
# Driver code
printNos(100)
 


# FIND FACTORIAL


def Fact(n):
    if n == 0:
        return 1
    else:
        return n * Fact(n-1)
print(Fact(5))


# ARITHMETIC FUNCTIONS USING FUNCTIONS


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print(add(10, 20))
print(sub(10, 20))
print(mul(10, 20))
print(div(10, 20))


# POWER OF 2


n = 10
p = 2

cal = list(map(lambda i: p ** i, range(n)))

for j in range(n):
   print(p," raised to power", j, "is", cal[j])




def sumofDigits(number):
    return number + number
print(sumofDigits(5))

