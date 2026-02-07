# =====================================================
# ENCAPSULATION
# =====================================================
# Encapsulation means wrapping data (variables) and
# methods (functions) into a single unit called a class.
# It also helps in DATA HIDING and controlled access.

# Access types in Python:
# public    → accessible anywhere
# protected → accessible inside class + subclass (_var)
# private   → accessible only inside class (__var)


class Bankaccount:
    def __init__(self, name, balance):
        self.name = name              # public attribute
        self.__balance = balance      # private attribute (data hiding)

    # getter method
    # used to access private data safely
    def get_balance(self):
        return self.__balance

    # setter method
    # used to update private data safely
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid balance")


# object creation
acc1 = Bankaccount("Rahul Kumar", 10000)

# accessing public data
print(acc1.name)

# accessing private data using getter
print(acc1.get_balance())

# modifying private data using setter
acc1.set_balance(200000)

print(acc1.get_balance())
