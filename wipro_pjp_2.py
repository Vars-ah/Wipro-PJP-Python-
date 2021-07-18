#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[3]:


b = 10
h = 20
area = 1/2 * b * h
print(area)


# In[5]:


a = 5
print("Type of a: ", type(a))
 
b = 5.0
print("\nType of b: ", type(b))
 
c = 2 + 4j
print("\nType of c: ", type(c))

d = " wipro"
print("\nType of d: ", type(d))


# In[6]:



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


# In[10]:


x = 5
y = 10
print("Before-->", x,y)
x , y = y , x
print("After -->",x , y)


# In[11]:


import math 
print(math.sqrt(4)) 


# In[13]:


a = 10
if a % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")


# In[15]:


celsius = float(input('Enter temperature in Celsius: '))  
fahrenheit = (celsius * 1.8) + 32  
print("C-->",celsius,"f-->",fahrenheit) 


# In[4]:


lists =['January', 'February', 'March', 'April', 'May', 'June', 'July',  'August', 'September', 
        'October', 'November', 'December']
for x in range(0,len(lists)):
 
    list = [x,lists[x]]
    print(list, end = "") 
    
    


# In[11]:


name = ['varsha', 'abu', 'lakshana','ramesh']
print("Length of list -->",len(name))
for i in name:
    print(i,end=" | ")

