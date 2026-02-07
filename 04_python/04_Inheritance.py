#=========== inheritance ===========
#Reusing attr & methods from a parent(base)class.


# Parent class
class Employee:
    start_time = "10am"   # class variable
    end_time = "6pm"      # class variable


# Child class (Inheritance)
# teacher inherits Employee
class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject   # instance variable


# object creation
t1 = Teacher("Math")

# accessing instance variable + inherited class variables
print(t1.subject, t1.start_time, t1.end_time)



#=========== Example ==========

# Parent class
# This class holds common data and methods for all employees
class employees:
    start_time = "12PM"   # class variable (shared by all employees)
    end_time = "1PM"

    # method to change end time
    def change_time(self, new_end_time):
        self.end_time = new_end_time


# Child class Teacher (inherits employees)
class Teacher(employees):
    def __init__(self, subject):   # constructor must be __init__
        self.subject = subject


# Child class AdminStaff (inherits employees)
class adminstaff(employees):
    def __init__(self, role):
        self.role = role


# object creation
staff1 = adminstaff("Manager")

# accessing instance variable + inherited class variables
print(staff1.role, staff1.start_time, staff1.end_time)
