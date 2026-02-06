#=========== ATTRIBUTES ========
#------>> Class & instance >>------

#class --->> which belongs to class ex.- college_name can be same
#instance --->> belongs to object ex.- name,subject,cgpa  can be different for all student

#example

class Student:
    college_name = "ABC College"

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


stu1 = Student("Tulshi", 9.2)

print(stu1.name)
print(Student.college_name)


# Note: when both class and instance have the same variable name,
# the instance variable gets higher priority

class Student1:
    college_name1 = "ABC College"
    PI = 3.1          # class attribute

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        self.PI = 3.14   # instance attribute (higher priority)


stu2 = Student1("Tulshi", 9.2)

print(stu2.name)
print(Student1.college_name1)
print(stu2.PI)





#========== Different type of methods ===========

# instance
# |
# | 1st parameter self
# | acess the class & instance attributes 

class laptop:
    storage_type = "ssd"

    def __init__(self,Ram,storage):
        self.Ram = Ram
        self.storaage = storage

    def get_info(self):
        print(f"laptop has{self.ram} ram & {self.storage}.{self.storage_type}")

    l1 = laptop("16gb", "512gb")
    l2 = laptop("8gb", "256gb")


#=============== class =================

# | 1 st parameter of class is cls
# | acess the only class attributes
# | decorator @classmethod ----->> a type of function which change the behaviour

#example

class Laptop:
    storage_type = "ssd"   # class variable

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):   # instance method
        print(f"Laptop has {self.ram} RAM & {self.storage} {self.storage_type}")


l1 = Laptop("16GB", "512GB")

l1.get_storage_type()
l1.get_info()


#================ Static ==============

# no compulsory parameter
# no acess of instance or class
# decorator @staticmethod --->>> 


class Laptop:
    storage_type = "ssd"

    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):  # instance method
        print(f"Laptop has {self.ram} RAM & {self.storage} {self.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"Discounted price = {final_price}")


l1 = Laptop("16GB", "512GB")

l1.get_storage_type()
l1.get_info()
l1.calc_discount(40_000, 10)




#======== practice problem ===============

# Product store
# Design & create an online store for Products (name, price).
# Track total products being created.
# Create a static method to calculate discount on each product based on a % parameter.

#++++++++++ step1-Product store ++++++++++++

# class product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price

#     def get_info(self):
#         print(f"price of {self.name} is Rs.{self.price}")

# p1 = product("phone", 10_000)
# p2 = product("laptop", 50_000)
# p3 = product("pen", 10)

# p1.get_info()



#+++++++++++.  step2-> track total product using classmethod +++++++++++++++++



# class product:
#     count = 0

#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         product.count += 1

#     def get_info(self): #instance methopd
#         print(f"price of {self.name} is Rs.{self.price}")

#     @classmethod
#     def get_count(cls):
#         print(f"total products in store = {cls.count}")

# p1 = product("phone", 10_000)
# p2 = product("laptop", 50_000)
# p3 = product("pen", 10)

# product.get_count()


#++++++++++++  step3-to calculate discount on each product based on a % parameter   +++++++++++++++++++++



