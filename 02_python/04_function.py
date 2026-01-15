#=========== function ===========
#              👇
#    Reusable component of code

#=--->>> Blocks of code that perform a specific task
#                                           👇
#                                   definition ---->> logic
#                                   call


# syntax ---->>

# def function_name():
#   code to run



#============= example ==========

def hello(): # fxn definition
    print("hello")
    print("from python")

hello() # fxn call

# fxn can be called many times

print("----------------------------------")


#function definition 
 
def sum(a,b): #parameters
    s = a + b
    return s

# function call
ans = sum(3,4)
print(ans)

print("----------------------------------")
#============== Example ==========

# calc average

def calc_avg(a,b,c):
    sum = a + b + c
    return sum/3

print(calc_avg(1,2,3))

print("----------------------------------")
#======= Default values in function ==========

def sum(a, b=1):
    return a + b

print(sum(5)) # output ==> 6

print("----------------------------------")
# def sum(a=1,b):
#     return a + b
# print(sum(5))        ---   # output ==> give error



#=============== LAMBDA FUNCTION ============

# lambda fnction is a small anymonus function

#📌 Syntax of lambda

#lambda arguments: expression

# it's can be many arguments but only one expression

sum = lambda a,b: a+b
print(sum(4,5))

print("----------------------------------")

avg = lambda a,b: (a+b)/2
print(avg(4,5))

print("----------------------------------")


#============ FACTORIAL OF N ===========

# n!----> 1*2*3*4*5*.........*n

# factorial logic

# def calc_factorial(n):
# fact = 1

# for i in range(1, n+1):
#     fact = fact*i

def calc_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i

    return fact

n = int(input("enter n: "))
print(calc_factorial(n))

print("----------------------------------")