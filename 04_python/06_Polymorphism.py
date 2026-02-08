#======= Polymorphism means-->> poly-many,phism-form
#____>>>diff meaning according to the context

#--->> operator overloading

# example-->
# print(a+b,"hello"+"world")

# function overriding(inheritance) redefing par class's fxn in child fxn

class Employees:
    def get_destignation(self):
        print("destigination = Employee")

class Teacher(Employees):#overriding
    def get_destiogination(self):
        print("destigination = Teacher")

t1 = Teacher()
t1.get_destignation()


#Duck Typing  
#walks like a duck * Quacks like a duck

class Teacher(Employees):
    def get_destigination(self):
        print("destigination = Teacher")

class Accountant():
    def get_destigination(self):
        print("destigination = Accountant")

t1 = Teacher()
t1.get_destigination()


acc1 = Accountant()
acc1.get_destigination()

    

