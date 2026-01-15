# LOOPS IN PYTHON
# doing the same work again and again without writing the code many times.

# ============== WHILE LOOP ==============
# A while loop keeps running again and again as long as a condition is true.

# 🍪 Real-life example
# While the fan is ON, it keeps running.
# When the fan is OFF, it stops.

# ============== INFINITE LOOP ==============
# while True:
#     print("hello world")
#     # stop it by pressing Ctrl + C


# BUT WE WANT "hello world" TO PRINT 5 TIMES
# so we use a COUNTER / ITERATOR

# ============== Example 1 ==============

i = 1   # initialize the value

while i <= 5:        # condition
    print(i)        # print numbers
    i += 1          # increment value

print("----------------------------------")

# ============== Example 2 ==============

count = 1

while count <= 5:
    print("hello world")
    count += 1      # increment value

print("----------------------------------")

#==========  EXAMPLE 2 =======

# PRINT IN REVERSE

count = 5 

while (count >= 1):
    print("count: ", count)

    count -= 1


print("----------------------------------")

# ========== MULTIPLICATION TABLE OF N ==========
n = int(input("enter num: "))

i = 1   # start from 1

while i <= 10:   # loop will run from 1 to 10
    print( n ,"*", i, "=", n * i)
    i += 1       # increase i by 1 each time

print("----------------------------------")






#=============== BREAK AND CONTINUE IN LOOPS ======================

# break ==>> break means >>>> terminate from the loop
# continue ==>> continue >>>> means skip the cureent values and execute next others


#======== Break =========

i = 1

while (i <= 10):
    if (i % 6 == 0):
        break
    print(i)

    i += 1 # updation ==>> if we forget updation then it's become infinite loop


print("----------------------------------")


#========== CONTINUE ===========

i = 1 

while (i <= 10):
    if (i % 3 == 0):
        i += 1
        continue # it's wll skip this value
    print(i)
    i += 1

print("----------------------------------")


#=========== ODD NUM ============

i = 1

while (i <= 10):
    print(i)
    i += 2  # incrimination by 2

print("----------------------------------")

#========== FOR LOOP ============

#>>>> A for loop is used when you want to repeat something a fixed number of times.

#   ==> sequential traversal 

string = "hello"

#in => membership operator

# syntax
# for (var) in collection:      =>> collection: list, string, or range.
    # code to run for each item

for var in string:
    print(var)



print("----------------------------------")

# in =>> to check presence

string = "Himanshu"

if "shu" in string:
    print("shu exist in Himanshu")

print("----------------------------------")


#============ for in range ===========

for i in range(5):
    print(i+1)

print("----------------------------------")

word = "artificial intelligence"

# count the number of i's ==> 5

ans = 0 

for ch in word:
    if(ch == 'i'):
        ans += 1

print("count of i =",ans)


print("----------------------------------")

#============ VOWELS COUNT ============

word = "artificial"

count = 0

for ch in word:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count += 1

print("ans =" , count)

print("----------------------------------")

#============= LOOPS IN RANGE ==========

# Range =>> sequence generate

# range(start,stop,step)

for i in range(1,6):
    print(i)

print("----------------------------------")


# ========== SUM OF FIRST N NATURAL NUMBERS =========

n = int(input("enter number: "))

sum = 0

for i in range(1,n+1):
    sum += i

print("sum =", sum)

