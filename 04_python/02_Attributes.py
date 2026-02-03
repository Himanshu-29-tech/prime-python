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
