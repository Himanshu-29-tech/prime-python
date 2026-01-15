# ============== TUPLES ================
# ===>> tuples are immutable sequence of values --> you can't change

tup = (1,2,3,4,5)

print(tup)
print(type(tup))
print(len(tup))
print(tup[2])

print("----------------------------------")

# tup[2] = 10  -->> it's give error  because it's immutable

#===========  TUPPLES METHODS ========

tup = (1,2,3,4,5)

for val in tup:
    print(val)

print("----------------------------------")


#====== print sum of tup =========

tup = (1,2,3,4,5)

sum = 0
for val in tup:
    sum += val

print(f"sum of vals is {sum}")

print("----------------------------------")


#--->> t.index(val) ===>>returns 1st occurence idx


tup = (1,2,3,4,5)

print(tup.index(2)) # it's return the position that's value is given in index(2) -->> that's 1

print("----------------------------------")
#--->> t.count(val) ===>>counts total occurences

tup = (1,2,3,2,4)

print(tup.count(2))

print("----------------------------------")