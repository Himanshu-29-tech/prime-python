# UNIT I

## 1. Setting up Programming Environment

**Python versions** — Abhi Python 3.x chalta hai (Python 2 discontinued ho chuka hai, 2020 mein support khatam). Exam mein agar version wala question aaye toh yaad rakho: **Python 3 hi standard hai**, print statement bina bracket ke Python 2 mein tha (`print "hi"`), Python 3 mein function hai (`print("hi")`).

**Python on Windows** — IDLE (Python ka default editor) install hota hai Python ke saath. Command line se `python filename.py` run karte hain, ya IDLE mein directly likh ke F5 dabate hain.

**Running 'Hello World'**
```python
print("Hello, World!")
```
Ye sabse pehla program hota hai — bas ek statement, `print()` function string ko output karta hai.

🎯 **TRICK**: Yaad rakhne ke liye — "**P**rint **H**ota **H**amesha **B**racket ke andar" (Python 3 mein `print` hamesha function hai, bracket compulsory).

---

## 2. Variables, Expressions, Statements

**Naming aur using variables**
- Variable = data store karne ka container. `x = 5` — yahan `x` naam hai, `5` value hai.
- Assignment operator `=` use hota hai (equal to check karne ke liye `==` use hota hai — ye confusion sabse common exam trap hai).

**Avoiding NameError**
- Agar variable use kiya bina define kiye toh `NameError: name 'x' is not defined` aata hai.
```python
print(y)   # NameError kyunki y kahin define nahi hua
y = 10
```

**Values aur Types**
- Har value ka ek type hota hai: `int` (5), `float` (5.5), `str` ("hello"), `bool` (True/False).
- `type(5)` → `<class 'int'>`

**Variable names aur keywords**
- Naam letter ya underscore se shuru hona chahiye, digit se nahi.
- Valid: `_name`, `name1`, `myVar`
- Invalid: `1name`, `my-var`, `class` (keyword hai)
- **33 reserved keywords** hote hain Python mein: `if, else, elif, for, while, def, class, return, import, True, False, None, and, or, not, in, is, break, continue, pass, try, except, finally, lambda, global, nonlocal, with, as, yield, assert, del, raise` — ye variable naam nahi ban sakte.

**Statements** — Ek complete instruction jo Python execute karta hai. `x = 5` ek statement hai.

**Operators aur Operands**
- Operand = value jis pe operation ho raha hai. Operator = symbol jo operation batata hai.
- `3 + 4` → `3` aur `4` operands hain, `+` operator hai.

**Order of Operations (Precedence)**
```
() sabse pehle
**  (exponent)
*, /, //, %  (left to right)
+, -  (left to right)
```
🎯 **TRICK**: **"PEMDAS"** yaad rakho — Parentheses, Exponent, Multiply/Divide, Add/Subtract.

**Operations on strings**
```python
"Himanshu" + " Yadav"   # concatenation -> "Himanshu Yadav"
"ab" * 3                  # repetition -> "ababab"
```
⚠️ String pe `-` ya `/` nahi chalta — sirf `+` (concat) aur `*` (repeat, sirf int ke saath).

**Composition** — Chhote expressions ko combine karke bada expression banana. Jaise `x = (a+b) * c`.

**Comments**
```python
# single line comment
'''
multi line
comment (actually a string, but used as comment)
'''
```

🎯 **BIG TRICK for Unit I**: Yaad rakho **"NAME-VALUE-TYPE"** cycle — pehle naam do (naming), fir value do (assignment), value ka apna type hota hai (int/float/str/bool). Ye cycle har programming language mein same hai.

---

# UNIT II

## 1. Conditional Statements

**Modulus operator `%`** — remainder deta hai. `10 % 3` = `1`.
- Even/odd check: `if n % 2 == 0: print("Even")`

**Random numbers**
```python
import random
random.random()        # 0.0 se 1.0 ke beech float
random.randint(1,6)    # 1 se 6 tak integer (dono included)
random.choice([1,2,3])  # list se koi bhi ek random element
```

**Boolean expressions** — Expression jiska result `True` ya `False` hota hai. `5 > 3` → `True`.

**Logic operators**
- `and` — dono True hone chahiye
- `or` — ek bhi True ho toh chalega
- `not` — reverse kar deta hai

🎯 **TRICK**: **AND = dono chahiye (strict), OR = koi bhi ek chalega (relaxed), NOT = ulta kar do**.

**Conditional (if-elif-else)**
```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```
⚠️ Python mein **indentation hi structure hai** — `{}` nahi hote. Galat indentation = `IndentationError`. Ye sabse common exam trap hai.

**Nested conditionals** — if ke andar if.
```python
if a > 0:
    if b > 0:
        print("Both positive")
```

## 2. Iterative Statements

**while loop** — Condition check hoti hai har baar, jab tak True hai loop chalta rahega.
```python
i = 0
while i < 5:
    print(i)
    i += 1
```
⚠️ Agar `i += 1` bhool gaye toh **infinite loop** ban jaayega — exam mein common bug-finding question.

**for loop**
```python
for i in range(5):     # 0,1,2,3,4 (5 EXCLUDED!)
    print(i)
```
🎯 **TRICK**: `range(start, stop, step)` mein **stop hamesha EXCLUDED hota hai**. Yaad rakho: "range dost banata hai stop se pehle tak, stop khud nahi aata."

**Nested for/while** — Loop ke andar loop. Pattern printing ke liye common.
```python
for i in range(3):
    for j in range(3):
        print(i,j)
```

**Random numbers in loops** — Dice simulation jaisa: loop chala ke har baar random number generate karna.

**Encapsulation aur Generalization**
- Encapsulation = logic ko function/block mein wrap karna taaki repeat na karna pade.
- Generalization = code ko is tarah likhna ki wo alag-alag input ke liye kaam kare, sirf ek fixed value ke liye nahi.

🎯 **BIG TRICK for Unit II**: **"WFN"** — **W**hile (condition check first), **F**or (range/sequence based), **N**ested (loop-in-loop for patterns). Teeno ka use-case yaad rakhne ke liye ye 3 letters kaafi hain.

---

# UNIT III — Functions & Recursion

**Function calls**
```python
def greet(name):
    print("Hello", name)

greet("Himanshu")   # function call
```

**Type conversion aur coercion**
- **Conversion (explicit)**: tum khud batate ho — `int("5")`, `str(5)`, `float("5.5")`.
- **Coercion (implicit)**: Python khud kar deta hai — `5 + 2.0` → `7.0` (int automatically float ban gaya).

🎯 **TRICK**: **C for Conversion = Coder karta hai (manual)**, **C for Coercion = Compiler karta hai (automatic)**.

**Math functions** (`import math` chahiye)
```python
math.sqrt(16)    # 4.0
math.floor(4.7)   # 4
math.ceil(4.2)     # 5
math.pow(2,3)       # 8.0
```

**Adding new function** — Apna khud ka function define karna `def` keyword se.

**Parameters aur Arguments**
- **Parameter** = function definition mein jo naam likha hai. `def f(x):` — yahan `x` parameter hai.
- **Argument** = function call mein jo actual value di. `f(5)` — yahan `5` argument hai.

🎯 **TRICK**: **"P for Plan (definition mein plan banate ho), A for Actual (call ke time actual value do)"**.

**Recursion aur uska use**
- Function khud ko call kare, base case ke saath (warna infinite recursion → `RecursionError`).
```python
def factorial(n):
    if n == 0:        # BASE CASE — ye hamesha hona chahiye
        return 1
    return n * factorial(n-1)   # RECURSIVE CASE
```

🎯 **BIG TRICK for Unit III**: Recursion yaad rakhne ke liye — **"Base case bina recursion, jaise seatbelt bina gaadi"** — kabhi mat bhoolo base case, warna crash (stack overflow) ho jaayega.

---

# UNIT IV

## 1. Strings (Compound Data Type)

**Length** — `len("hello")` → `5`

**String traversal**
```python
for ch in "hello":
    print(ch)
```

**String slices** — `s[start:stop]`, stop excluded.
```python
s = "Himanshu"
s[0:4]     # "Hima"
s[-3:]      # last 3 chars
s[::-1]      # reverse
```

**Comparison** — `==` value compare karta hai (alphabetically, ASCII values ke basis pe).
```python
"apple" < "banana"    # True (a < b in ASCII)
```

**find function**
```python
"hello".find("l")   # 2 (pehla occurrence ka index)
"hello".find("z")   # -1 agar nahi mila
```

**Looping and counting**
```python
count = 0
for ch in "banana":
    if ch == "a":
        count += 1
```

⚠️ **Strings IMMUTABLE hote hain** — `s[0] = 'J'` karoge toh **TypeError** aayega. Ye **sabse common MCQ/theory question** hai exam mein.

## 2. Lists

**List values** — `[1, 2, "three", 4.0]` — mixed type allowed hai.

**Length** — `len(lst)`

**Membership** — `3 in lst` → True/False

**Operations**
```python
lst = [1,2,3]
lst + [4,5]     # concatenation
lst * 2           # repetition
```

**Slices** — string jaise hi: `lst[1:3]`

**Deletion**
```python
lst.remove(2)    # value 2 remove
del lst[0]         # index 0 remove
lst.pop()           # last element remove aur return karega
```

**Accessing elements** — `lst[0]`, `lst[-1]`

**List and for loops**
```python
for item in lst:
    print(item)
```

**List parameters aur nested list**
- Lists **mutable** hain — function mein pass karo toh original list bhi change ho sakti hai (pass by reference jaisa behavior).
```python
def add_item(l):
    l.append(100)

my_list = [1,2,3]
add_item(my_list)
print(my_list)   # [1,2,3,100] — original CHANGE ho gaya!
```
- Nested list = `[[1,2],[3,4]]` — list ke andar list.

🎯 **TRICK**: **"Lists LIVE (mutable), Strings STATIC (immutable)"** — Lists ko baar-baar modify kar sakte ho, strings ko nahi (naya string banana padta hai).

## 3. Tuples aur Dictionaries

**Mutability aur Tuples** — Tuples **immutable** hote hain, ek baar bana diya toh change nahi kar sakte.
```python
t = (1,2,3)
t[0] = 5   # TypeError!
```

**Tuple assignment**
```python
a, b = 1, 2      # multiple assignment
a, b = b, a        # SWAP trick — bina temp variable ke!
```

**Tuple as return values** — Function ek saath multiple values return kar sakta hai (actually tuple return karta hai).
```python
def minmax(lst):
    return min(lst), max(lst)

low, high = minmax([3,1,4,1,5])
```

**Dictionaries — operations aur methods**
```python
d = {"name": "Himanshu", "age": 20}
d["city"] = "Phagwara"    # add
d["age"] = 21                # update
del d["age"]                   # delete

d.keys()      # dict_keys(['name', 'city'])
d.values()     # dict_values(['Himanshu', 'Phagwara'])
d.items()       # key-value pairs
d.get("name")     # safe access — None agar key nahi mili
```

**Sparse matrices** — Bahut saari zero/empty values wali matrix ko dictionary se represent karna, sirf non-zero values store karke memory bachana.
```python
sparse = {(0,1): 5, (2,3): 7}   # baaki sab zero maan lo
```

**Aliasing aur Copying**
- **Aliasing**: Do variables same object ko point karte hain. Ek change karo toh dusra bhi change ho jaata hai.
```python
a = [1,2,3]
b = a          # aliasing — same object
b.append(4)
print(a)        # [1,2,3,4] — a bhi change ho gaya!
```
- **Copying**: Independent copy banani ho toh `.copy()` use karo.
```python
b = a.copy()    # ab b independent hai
```

🎯 **BIG TRICK for Unit IV**: 
- **"STL"** yaad rakho — **S**trings immutable, **T**uples immutable, **L**ists mutable (dict bhi mutable).
- Swap trick: **`a,b = b,a`** — exam mein directly puch sakte hain "temp variable ke bina swap karo".

---

# UNIT V — Classes and Objects (OOP)

**Creating classes**
```python
class Student:
    def __init__(self, name, roll):   # constructor
        self.name = name
        self.roll = roll
```

**Creating instance objects**
```python
s1 = Student("Himanshu", 67)    # object banaya
```

**Accessing attributes**
```python
print(s1.name)    # Himanshu
print(s1.roll)      # 67
```

## OOP Terminology

**Class** — Blueprint/template. (Jaise "Student" class ek design hai).
**Object** — Class ka actual instance. (`s1` ek object hai jo Student class se bana).

**Inheritance** — Ek class dusri class ke properties/methods use kar sakti hai.
```python
class Person:
    def greet(self):
        print("Hello")

class Student(Person):    # Student inherits from Person
    pass

s = Student()
s.greet()    # "Hello" — Person ka method mil gaya bina rewrite kiye
```

**Overriding Methods** — Child class parent ke method ko apne hisaab se redefine kar sakti hai.
```python
class Person:
    def greet(self):
        print("Hello from Person")

class Student(Person):
    def greet(self):               # OVERRIDING
        print("Hello from Student")

s = Student()
s.greet()    # "Hello from Student" — child ka version chala
```

**Data Hiding** — `__` (double underscore) prefix se attribute ko "private" bana dete hain (name mangling).
```python
class Account:
    def __init__(self):
        self.__balance = 1000    # private attribute

a = Account()
print(a.__balance)     # AttributeError — directly access nahi kar sakte
```

**Function Overloading** — Same naam ke multiple functions, different parameters ke saath.
⚠️ **IMPORTANT EXAM POINT**: Python **natively function overloading support NAHI karta** — jo bhi last definition hogi wahi use hogi, purani overwrite ho jaayegi. Ye ek **classic True/False MCQ** hai.
```python
def add(a,b):
    return a+b
def add(a,b,c):     # ye purane "add" ko OVERWRITE kar dega
    return a+b+c

# add(2,3) ab ERROR dega kyunki naya add 3 arguments maangta hai
```

🎯 **BIG TRICK for Unit V**: **"C-O-I-D-O"** yaad rakho:
- **C**lass = blueprint
- **O**bject = actual cheez
- **I**nheritance = property child ko milti hai
- **D**ata hiding = `__` se private
- **O**verriding = same naam, child version chalta hai (overloading Python mein nahi hota — ye ulta yaad rakho: "**O**verloading **O**absent hai Python mein")

---

# UNIT VI — Files, Exceptions, Regex

## 1. Text Files

**Writing variables to file**
```python
f = open("data.txt", "w")
f.write("Himanshu\n")
f.close()
```

**Reading from a file**
```python
f = open("data.txt", "r")
content = f.read()          # poora file ek string mein
line = f.readline()          # ek line
lines = f.readlines()          # list of lines
f.close()
```

**Writing to a file**
```python
with open("data.txt", "a") as f:   # 'a' = append mode
    f.write("New line\n")
```

**Directories**
```python
import os
os.getcwd()          # current directory
os.listdir()           # list of files/folders
os.mkdir("new_folder")  # naya folder banao
```

**Pickling** — Python object ko binary file mein directly save karna (serialization).
```python
import pickle
data = {"name": "Himanshu"}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)          # save

with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)        # load back
```

🎯 **TRICK**: File modes yaad rakhne ke liye — **"RWA"**: **R**ead (existing file chahiye), **W**rite (overwrite/create), **A**ppend (end mein add karta hai, delete nahi karta).

## 2. Exception Handling

**Handling ZeroDivisionError**
```python
try:
    x = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**try-except blocks**
```python
try:
    risky_code()
except SpecificError:
    handle_it()
except:                          # catch-all (sab errors)
    print("Something went wrong")
```

**The else block** — Sirf tab chalta hai jab try mein koi exception NA aaye.
```python
try:
    x = 10/2
except ZeroDivisionError:
    print("Error")
else:
    print("No error, this ran!")    # ye chalega kyunki koi error nahi aayi
finally:
    print("This ALWAYS runs")        # chahe error aaye ya na aaye
```

**Handling FileNotFoundError**
```python
try:
    f = open("nofile.txt", "r")
except FileNotFoundError:
    print("File doesn't exist!")
```

🎯 **TRICK**: **"TEEF"** — **T**ry (risky code), **E**xcept (error handle), **E**lse (agar sab theek), **F**inally (hamesha chalega).

## 3. Regular Expressions

**Concept** — Pattern-matching ka tareeka text mein specific format dhoondhne ke liye (jaise email, phone number).

**Types of patterns**
| Symbol | Matlab |
|---|---|
| `\d` | digit (0-9) |
| `\w` | word character (letter/digit/underscore) |
| `\s` | whitespace |
| `.` | koi bhi single character |
| `*` | 0 ya zyada baar |
| `+` | 1 ya zyada baar |
| `^` | string ka start |
| `$` | string ka end |

**match function**
```python
import re
re.match(r"\d+", "123abc")     # start se match karta hai -> matches "123"
re.match(r"\d+", "abc123")     # None -> kyunki start mein digit nahi hai
```

**search vs match** — ⚠️ **Bahut common exam question**:
- `re.match()` — sirf **string ke START** pe check karta hai.
- `re.search()` — **poore string mein kahin bhi** dhoondhta hai.
```python
re.search(r"\d+", "abc123")     # matches "123" — search poore string me dhoondhta hai
re.match(r"\d+", "abc123")       # None — match sirf start check karta hai
```

**Web Scraping using Regular Expressions** — Websites/HTML text se specific pattern (jaise email address, links) regex se nikalna.
```python
text = "Contact: himanshu@email.com"
emails = re.findall(r"[\w.]+@[\w.]+", text)
```

🎯 **BIG TRICK for Unit VI**: **"MS"** yaad rakho — **M**atch = **S**tart only, **S**earch = **S**omewhere anywhere. ("Match ki M, Start ki S — dono match karte hain shuru se")

---

# 🔑 MASTER MEMORY TABLE (Exam se pehle 5 min mein revise karo)

| Concept | Trick |
|---|---|
| `//` floor division | Negative mein neeche jaata hai: `-5//2 = -3` |
| Strings | IMMUTABLE — modify nahi ho sakti |
| Lists | MUTABLE — modify ho sakti hai, function mein change reflect hota hai |
| Tuples | IMMUTABLE — banane ke baad fix |
| `range(a,b)` | `b` EXCLUDED hota hai |
| `and`/`or` | and=dono chahiye, or=ek chalega |
| Recursion | Base case ke bina = crash |
| Function overloading | Python mein NATIVE support NAHI hai |
| `is` vs `==` | is=same memory location, ==value same hai |
| `match()` vs `search()` | match=start only, search=anywhere |
| try-except-else-finally | else=no error hua toh, finally=hamesha chalega |
| Pickling | Object ko binary file mein save karna |
| Swap trick | `a,b = b,a` — bina temp ke |
| `__init__` | Constructor, object banate hi auto-call hota hai |
| `self` | Current object ka reference, hamesha pehla parameter |
| Data hiding | `__` double underscore se private banta hai |

---
