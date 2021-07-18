#!/usr/bin/env python
# coding: utf-8

# PRINT HELLO WORLD


print("Hello World")


# FIND AREA OF THE TRIANGLE


b = 10
h = 20
area = 1/2 * b * h
print(area)


# PRINT VARIOUS DATATYPES

a = 5
print("Type of a: ", type(a))
 
b = 5.0
print("\nType of b: ", type(b))
 
c = 2 + 4j
print("\nType of c: ", type(c))

d = " wipro"
print("\nType of d: ", type(d))


# OPERATORS


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


# SWAP TWO NUMBERS


x = 5
y = 10
print("Before-->", x,y)
x , y = y , x
print("After -->",x , y)


# FIND THE SQUARE ROOT


import math 
print(math.sqrt(4)) 


# DIVISIBILITY BY 5


a = 10
if a % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")


# CONVERT TEMPERATURE TO CELSIUS


celsius = float(input('Enter temperature in Celsius: '))  
fahrenheit = (celsius * 1.8) + 32  
print("C-->",celsius,"f-->",fahrenheit) 


# PRINT NUMBERS NAMES AND MONTHS

lists =['January', 'February', 'March', 'April', 'May', 'June', 'July',  'August', 'September', 
        'October', 'November', 'December']
for x in range(0,len(lists)):
 
    list = [x,lists[x]]
    print(list, end = "") 
    
    


# PRINT NAME AND NUMBER
name = ['varsha', 'Alya', 'Dakshana']
print("Length of list -->",len(name))
for i in name:
    print(i,end=" | ")

