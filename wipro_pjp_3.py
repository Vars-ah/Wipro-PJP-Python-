#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = 23
if a >= 25:
    print("Enjoy Marriage Life")
else:
    print("Enjoy Bachelor Life")


# In[8]:


a = 2001
if a % 4 == 0 and a % 400 != 0 or a % 100 == 0:
    print("Leap:",a)
else:
    print("Not Leap Year:",a)


# In[12]:


a = 10
b = 20 
c = 30
sum = a + b + c
if a == b or b == c or c == a:
    sum  = 0 
    print(sum)
else:
    print(sum)


# In[14]:


def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b / gcd(a, b)
print(gcd(10,20))
print(lcm(10,20))


# In[19]:


a = 10
if a > 0:
        print("Positive Number")
elif a < 0:
        print("Negative Number")
elif a == 0:
        print("Zero")
        
start = 10
end = 25
for i in range(start, end, 3):
    print(i, end = " ")


# In[1]:


n = 10
a = 0
b = 1
count = 1
sum = 0
while count < n:
    print(sum, end = " ")
    count += 1
    a = b
    b = sum
    sum = a + b


# In[2]:


start = 25
end = 75
for i in range(start, end+1):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i, end = " ")


# In[3]:


n = 19
for i in range(0,n):
    print(i, end = " || ")
    
# same number
print("\n",(str(10)+' ') * 5)


# In[4]:


even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0
total = 0

while True:
    num = int(input("Input an integer (0 terminates): "))
    if num == 0:
        break
    if num < 1:
        continue
    if num % 2 == 0:
        even_count += 1
        even_sum += num
    else:
        odd_count += 1
        odd_sum += num
    total += 1

print("")
print("Sum of odds:", odd_sum)
print("Sum of evens:", even_sum)
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Total positive int count:", total)


# In[6]:


My_Number = 12345
Reverse_Number = 0
while(My_Number > 0):
    Reminder = My_Number %10
    Reverse_Number = (Reverse_Number *10) + Reminder
    My_Number = My_Number //10
print(Reverse_Number)


# In[ ]:




