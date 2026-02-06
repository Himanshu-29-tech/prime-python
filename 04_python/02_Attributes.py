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

class laptop:
        storage_type = "ssd"


def __init__(self,Ram,storage):
    self.Ram = Ram
    self.storage = storage

@classmethod
def get_storage_type(cls):
    print(f"storage type = {cls.storage_type}")

def get_info(self): #instance method
    print(F"laptop has{self.Ram} Ram & {self.storage} {self.storage_type}")


l1 = laptop("16gb" , "512gb")

l1.get_storage_type()



#================ Static ==============

# no compulsory parameter
# no acess of instance or class
# decorator @staticmethod --->>> 


class laptop:
        storage_type = "ssd"


def __init__(self,Ram,storage):
    self.Ram = Ram
    self.storage = storage

@classmethod
def get_storage_type(cls):
    print(f"storage type = {cls.storage_type}")

def get_info(self): #instance method
    print(f"laptop has{self.Ram} Ram & {self.storage} {self.storage_type}")

@staticmethod
def clc_discount(price,discount):
    final_price = price - (discount * price / 100)
    print(f"discounted price = {final_price}")

l1 = laptop("16gb" , "512gb")

l1.calc_discount(40_000,10)
