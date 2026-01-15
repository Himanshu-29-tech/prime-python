# ================= IF CONDITION =================
age = int(input("Enter your age: "))

# if condition is true, this part will run
if age == 18:
    print("You can vote")
    print("You can drive")

print("----------------------------------")

# ================= IF - ELSE =================
age = int(input("Enter your age again: "))

if age == 18:
    print("You can vote")
else:
    # if condition is false, this part will run
    print("You can't vote")

print("----------------------------------")

# ================= IF - ELIF - ELSE (Traffic Light) =================
color = input("Enter traffic light color: ")

if color == "red":
    print("Stop")

elif color == "green":
    # checked when first condition is false
    print("Go")

elif color == "yellow":
    print("Look")

else:
    # runs when no condition is true
    print("Wrong color for traffic light")

print("----------------------------------")

# ================= IF - ELIF - ELSE (Age Group) =================
age = int(input("Enter your age to check group: "))

if age < 13:
    print("You are a child")

elif age >= 13 and age < 18:
    # age between 13 and 17
    print("You are a teenager")

else:
    print("You are an adult")

print("----------------------------------")


 # ================= IF - ELIF - ELSE (USERNAME) ===============

username = input("enter username: ")
password = input("enter passwords: ")

if (username == "admin" and password == "pass"):
    print("LOGIN SUCESSFUL!")
elif (username != "admin"):
    print("wrong username")
else:
    print("wrong password")

print("----------------------------------")

# ================ example multiple or not  =============

n = int(input("enter num: "))

if (n% 5 == 0):
    print("multiple of 5")
else:
    print("not multiple of 5")


print("----------------------------------")

# ========== ODD OR EVEN ==========

# IF ANY NUMBER IS DIVISIBLE BY 2 THEN IT'S EVEN NUMBER
# IF ANY NUMBER IS NOT DIVISIBLE BY 2 THEN IT'S ODD NUMBERS

num = int(input("Num: "))

if (num % 2 == 0) :
    print("it's even number")
else:
    print("it's odd number")

print("----------------------------------")
# =========== NESTING =========

# 💁Nesting = if inside if
# 💁Used when you need to check one more condition after the first one is true

username = input("enter username: ")
password = input("enter passwords: ")

if (username == "admin" and password == "pass"):
    print("sucess")
else:                  # if inside if 
    if (username != "admin"):
        print("wrong usernme")
    else:
        print("wrong password")

print("----------------------------------")

# ==========KEY POINT =======

# you can write multiple if-if-if condition
# single if can be written
# byt elif  amd else exist only with if 
