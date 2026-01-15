#================ LISTS ==============

#------>>>>> lists are mutable 

marks = [99, 89 , 100 , 65, 92]

print(marks) 
print(len(marks)) # it print length of list
print(marks[0]) 
print(marks[1]) # you can aslo access the index value

print("----------------------------------")


#================ SLICING ============

# same as string slice

marks = [99, 89 , 100 , 65, 92, "abc", 100.99]

print(marks[-5:2])

print("----------------------------------")


# In Python lists (and strings):
# ✅ Starting index is 0
# ✅ Last index is -1

#===================== LISTS METHODS ===============


# l.append(val) --->> add one element at the end
# l.insert(idx,val)  --->> insert element at idx
# l.sort()  ---->> arranges in increasing order
# l.reverse()  --->> reverses order


#============= APPEND ===========

nums = [1,2,3]

nums.append(4)

print(nums)

print("----------------------------------")


nums.insert(2,10) # at index 2 value 10 will be inserted
print(nums)

print("----------------------------------")


nums.sort()
print(nums)

print("----------------------------------")


nums.reverse()
print(nums)

print("----------------------------------")


#================ LOOP IN LIST ==============

nums = [1,2,3,4]

for val in nums:
    print(val)

print("----------------------------------")


#==============  EXAMPLE  ===========
#----->> linear search 


nums = [1,2,3,4,5,6]

x = 10
idx = 0

for val in nums:
    if(val == x):
        print(f"x found at idx={idx}")
        break
    idx += 1

print("----------------------------------")
