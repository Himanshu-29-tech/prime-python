#============= OOP ==============

# OOP means Object-Oriented Programming.
# It is a way of writing programs by using objects just like real-life things.

#===== object =========== 

# An object is a real thing.
# Example: Car, Student, Mobile
# In programming, an object has:
# Data (properties)
# Work (functions)

#====== Class ============

# A class is a blueprint of an object.
# 👉 Like:
# Class = Design of a house
# Object = Real house built from that design


# class ClassName:
#     # constructor
#     def __init__(self, data1, data2):
#         self.data1 = data1
#         self.data2 = data2

#     # method
#     def show(self):
#         print(self.data1, self.data2)

class Student:
    subject = "python"
    college = "ABC"
    year = "4th year"

stu1 = Student()
stu2 = Student()

print(stu1.subject, stu1.college, stu1.year)
print(stu2.subject, stu2.college, stu2.year)




#============= ATTRIBUTES AND METHODS ==============

# A class (blueprint) has properties and behaviours.
# In easy words:
# Properties → what it has
# 👉 name, age, color, speed
# Behaviour → what it does
# 👉 run(), eat(), study(), drive()

class Car:          # blueprint
    color = "Red"   # property

    def drive(self):   # behaviour
        print("Car is driving")



# ================= Constructor =================
# __init__ method → initializes values when an object is created

class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa


# Creating objects of the class
stu1 = Student("Rahul", 8.2)
stu2 = Student("Shradha", 7.9)
stu3 = Student("Utkarsh", 8.5)
stu4 = Student("Himanshu", 7.6)


# =========== TYPE OF CONSTRUCTOR =========
# Parameterized Constructor example

class Student:
    def __init__(self, name, cgpa):   # parameterized constructor
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa


stu1 = Student("Rahul", 8.2)
stu2 = Student("Shradha", 7.9)
stu3 = Student("Utkarsh", 8.5)

print(stu1.get_cgpa())


