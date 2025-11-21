print("hello world")

# variable
_name="Himanshu"
age = 18

print(_name,age)

# data type
name="Ram"
age=18
price=25.38

print(type(name))
print(type(age))
print(type(price))

# boolean-true/false

# print(type(isPrime)) #false = 123

#comment in python
# use kro
#for multiline use triple quote
'''
multi line 
cooment
'''
# style guide - chizo ko likhne ka tarika
total_prize = 100# snake case{underscore used and rest all text are lowercase}
totPrice = 100# camel case{first word ka first later will be smal and rest all  first later are uppercase}
TotPrize = 100# pascal case{ all first letter are capital}

#use snake case for python

tot_price = 500
full_name = "Himanshu"

#writ a program to sum two numbers?
a=5
b=10

sum=a+b
print(sum)

#operators in python
a=9
b=5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)#modulo {gives remainder value}
print(a**b)#power


#comparision operators
a = 10
b = 5
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)
print(a == b)

#assignment operators
a = 50 #assign with = 

#using +=
b = 5
#b =b+1 {b ki value ke andar  b ko + ya - karke store kr diya}
b += 5
b -= 5
b *= 5
b **= 5
print(b)


#relational operators
var = 45
print(not (var))# not used to reseve the result

print((5 > 3) and (3 > 8)) #and
print((5 > 3) or (3 > 8))#or





#operators precedence - priority order of operators in a single line
'''
order  similar to bodomas rule
()
**
*,/,%
+,_
==,!=,>,>=,<,<=
not
and
or
if same precedence then goes to left to wright in line
'''



#type convrsion
a,b = 1,2.0
sum = a+b
print(sum)#python automatically change int to float

ans = int(1 + 2.0)
print(ans)# python ko forcefully int me convert karwaya gya hai

print(int("123"))
print(bool(10))# true=1,flase = 0 



#input valur in python 
a = input("enter value of a:")
print("welcome",a)

b = input("enter a: ")
c = input("enter b: ")
sum = b+c
print(sum)#gives string result

b = int(input("enter a: "))
c = int(input("enter b: "))
sum = b+c
print(sum)#gives sum result


#print the average of 2 numbers
a = int(input())
b = int(input())
average = (a+b)/2
print(average)


#assigment1
#Write a program that asks the user for their name and age,then print a sentence like:
name=input("write your name:")
age=int(input("write your age:"))
print("hello", name, ",you are", age, "years old!")


#Take two numbers as  input from the user and print their. sum,difference,product,and quotien
a=int(input("first number:"))
b=int(input("second number"))

sum = a+b
diff = a-b
product = a*b
quotient = a/b 
print(sum)
print(diff)
print(product)
print(quotient)

#Ask the user to enter two integer and one float.Convert them all to floats and print their average
a=int(input("enter a:"))
b=float(input("enter b:"))
average=(a+b)/2
print(float(average))

#The user enter s a string containing a number(e.g.,).Convert it to:"45"•an integer•a float•a string again Print all three values with their types
a=input("enter a string containg a number: ")
print(int(a))
print(float(a))
print(str(a))
print(type(int(a)))
print(type(float(a)))
print(type(str(a)))

# x = 10+3*2**2
a=10
b=3
c=2
print((a+b) * c ** c)

#swap two number
a = int(input("enter a:"))
b = int(input("enter b:"))
a,b = b,a
print(a,b)

#Ask the user for a temprertaure in a ccelsius(srtring inuput).convert it to float,then calculate and print temperature in farehnheit.
CelsiusTemp = input("temperature in celsius: ")
CelsiusTemp = float(CelsiusTemp)
fahrenheitTemp = (CelsiusTemp*(9/5))+32
print(fahrenheitTemp)

#Take the radius(r) as user input and print the area

r = int(input("r:"))
pie = 3.14
area = pie*r**2


#Ask the user for: principle ,rate ,time, cob=nvert to all float
p=int(input("take the p: "))
r=int(input("takr the rate: "))
t=int(input("take the time: "))
simple_interest=(p*r*t)/100
print(float(simple_interest))

# TAke a decimal number as input like 45.78 and output its:
a = float(input("take a decimal number"))
print(int(a))
