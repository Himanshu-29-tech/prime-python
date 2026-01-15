#======== PROBLEM 1 =========

salary = int(input("write your sallery: "))

if (salary < 30,000):
    print("fix tax rate 5%")
elif (salary == 30,000 or salary == 70,000):
    print("fix tax rate 15%")
else:
    print("fix rate is 25%")




#=========== PROBLEM2 =============

a = int(input("a: "))

b = int(input("b: "))

i = 0

for i in range(a,b):
    i += 1
    if (i % 2 == 0):
        print("even number: ",i)


#=========== problem3 =============
digits = int(input("Write three digit num: "))
for i in range(digits):
    print(i)