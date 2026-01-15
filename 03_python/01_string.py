# ========== STRING ==========

# string ==>>> store the sequence of characters

word = "python"

print(len(word))

#========== Concatenation ===========

word1 = "I love"
word2 = "python"

#concatenate
print(word1 + " " + word2)


# ============ INDEXING IN STRING ===========

word = "Rowdy"

print(word[0])


# sring are immutable--->> you can't change

# word = "python"

# word[2] = 'h'

# print(word[2]) # it's give error



#=========== SLICING IN STRING ===========

# syntax
# text[start : end : step]   -->># output not included end idx

# | Code           | Result                      |
# | -------------- | --------------------------- |
# | `s[:]`         | whole string                |
# | `s[start:]`    | from start index to end     |
# | `s[:end]`      | from beginning to end index |
# | `s[start:end]` | between start & end         |
# | `s[::step]`    | skip with step              |
# | `s[::-1]`      | reverse string              |
# | `s[-n:]`       | last n characters           |
# | `s[:-n]`       | remove last n characters    |

name = "developer"

print(name[:4])      # 'deve'
print(name[4:])      # 'loper'
print(name[-3:])     # 'per'
print(name[::2])     # 'dvlpr'
print(name[::-1])    # 'repoleved'


#===============  STRING FORMATTING =============
#=====>>> when we used dynamic strings --->>> diff var & value

# format()
a = 5
b = 10

sum = a + b

#normal formatting
print("language is {}".format("python"))
print("sum is {}".format(sum))
print("sum of {} & {} is {}".format(a,b,sum))



#index based formatting
print("sum of {1} & {0} is {2}".format(a,b,sum))


#============== F-strings ==============
#------>>> Literal string interpolation

# syntax

#----->>>  f"string {variable}"

a = 5
b = 15

print(f"sum of {a} & {b} is {a+b}")
print(f"avg of {a} & {b} is {a+b/2}")
