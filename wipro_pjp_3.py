

#SIMPLE IF-ELSE PROGRAM
a = 23
if a >= 18:
    print("Enjoy Marriage Life")
else:
    print("Enjoy Bachelor Life")


# FIND LEAP YEAR


a = 2001
if a % 4 == 0 and a % 400 != 0 or a % 100 == 0:
    print("Leap:",a)
else:
    print("Not Leap Year:",a)


# PRINT SUM, IF SAME VARIABLES PRINT 0


a = 10
b = 20 
c = 30
sum = a + b + c
if a == b or b == c or c == a:
    sum  = 0 
    print(sum)
else:
    print(sum)


# FIND GCD AND LCM

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b / gcd(a, b)
print(gcd(10,20))
print(lcm(10,20))


# DETECT TYPE OF NUMBES


a = 10
if a > 0:
        print("Positive Number")
elif a < 0:
        print("Negative Number")
elif a == 0:
        print("Zero")
        



# PRINT 10 FIBONACCI NUMBER
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


# PRINT PRIME NUMBER BETWEEN CERTAIN RANGES


start = 25
end = 75
for i in range(start, end+1):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i, end = " ")


# REPEAT NUMBER TILL THE GIVEN NUMBER


n = 19
for i in range(0,n):
    print(i, end = " || ")
    
# same number
print("\n",(str(10)+' ') * 5)


# LOOP UNTIL USER INPUT 0


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


# REVERSE OF INTEGER


My_Number = 12345
Reverse_Number = 0
while(My_Number > 0):
    Reminder = My_Number %10
    Reverse_Number = (Reverse_Number *10) + Reminder
    My_Number = My_Number //10
print(Reverse_Number)



