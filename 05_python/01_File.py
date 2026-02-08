#========= File Input/Output ============

# open,read & close
#open-->> syntax
# f = open("file_name","r")

f = open("05_python/sample.txt", "r") # file object
data = f.read()
print(data)
print(type(data))

f.close()


# write

f = open("05_python/sample.txt", "w")
f.write("123")
f.close()
