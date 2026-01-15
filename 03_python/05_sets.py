#============== sets ==============
#--->> collection of unique elements

# sets is itself mutable and unordered
# but element of sets are immutable

s = {1,2,3,4,5}

s.add(6)

print(s)

print("----------------------------------")
#================ EMPTY SETS =============

empty_set = set()

print(type(empty_set))

print("----------------------------------")
#================{} ===============

#=============== SET METHODS ============

# s.add(val)  -->adds a val
# s.remove(val)   -->remove a val
# s.clear()     -->empties the set
# s.pop()     -->removes a random val
# s.union(set2)     -->returns new union
# s.intersection(set2)   --> returns new intersection


# Create a set
s = {1, 2, 3}
set2 = {3, 4, 5}

# 1. add() → adds a value
s.add(10)
print("After add:", s)
# Output: {1, 2, 3, 10}

print("----------------------------------")
# 2. remove() → removes a value
s.remove(2)
print("After remove:", s)
# Output: {1, 3, 10}


print("----------------------------------")
# 3. clear() → empties the set
temp = {1, 2, 3}
temp.clear()
print("After clear:", temp)
# Output: set()

print("----------------------------------")

# 4. pop() → removes a random value
popped_value = s.pop()
print("Popped value:", popped_value)
print("After pop:", s)


print("----------------------------------")

# 5. union() → returns a new set with all values
u = s.union(set2)
print("Union:", u)
# Output: {1, 3, 4, 5, 10}


print("----------------------------------")

# 6. intersection() → returns common values
i = s.intersection(set2)
print("Intersection:", i)
# Output: {3}

print("----------------------------------")


#============== PROBLEM ================

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

result = {}   # dictionary to store data

for name, course in info:
    if name not in result:
        result[name] = set()   # create empty set for new name
    result[name].add(course)  # add course to the set

print(result)

print("----------------------------------")

# 📊 Quick Comparison Table

# | Feature           | List | Tuple | Dictionary | Set  |
# | ----------------- | ---- | ----- | ---------- | ---- |
# | Syntax            | `[]` | `()`  | `{k:v}`    | `{}` |
# | Ordered           | ✅   | ✅    | ✅*        | ❌    |
# | Changeable        | ✅   | ❌    | ✅         | ✅    |
# | Allows Duplicates | ✅   | ✅    | ❌ (keys)  | ❌    |
# | Indexing          | ✅   | ✅    | ❌         | ❌    |
# | Key-Value Pair    | ❌   | ❌    | ✅         | ❌    |
