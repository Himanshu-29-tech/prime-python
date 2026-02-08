#====== List comprehensions ========
#--->>
# output for item in iterable if condition


squares = []

for i in range(6):
    squares.append(i*i)

print(squares)

# using list comprehensions

sq = [i*i for i in range(6)]
print(sq)


# odd number

sq = [i*i for i in range(6) if i%2 != 0]
print(sq)

#using if-else condition

nums =[-2,-3,3,4,-1,7]

nums = [0 if val < 0 else val for val in nums]
print(nums)
