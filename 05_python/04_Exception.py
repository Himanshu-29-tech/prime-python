#======= Exception Handling =========
#---->>> Try,except,else,finally

#--->> what are the error can be in program and how we can manage it

#try

try:
    x = int(input("enter x: "))
    ans = 10/x

except ZeroDivisionError:
    print(f"Divide by 0 is not allowed")

except ValueError:
    print(f"Invalid input")

else:
    print(f"ans = {ans}")

finally:
    print("End of program")