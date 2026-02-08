# ================= FILE INPUT / OUTPUT (ALL IN ONE) =================

# -------- 1. READ FILE --------
print("----- Reading File -----")
f = open("05_python/sample.txt", "r")
data = f.read()
print(data)
print(type(data))     # <class 'str'>
f.close()


# -------- 2. WRITE FILE (Overwrite) --------
print("\n----- Writing File (w mode) -----")
f = open("05_python/sample.txt", "w")
f.write("123")
f.close()


# -------- 3. APPEND FILE --------
print("\n----- Appending File (a mode) -----")
f = open("sample.txt", "a")
f.write("\nnew text being appended\n to the file")
f.close()


# -------- 4. CREATE NEW FILE --------
print("\n----- Creating New File (x mode) -----")
f = open("sample_new.txt", "x")
f.write("some random text")
f.close()


# -------- 5. READ FILE AGAIN --------
print("\n----- Reading Updated File -----")
f = open("sample.txt", "r")
print(f.read())
f.close()


# ================= FILE MODES SUMMARY =================
"""
r  -> Read (default)
w  -> Write (overwrite file)
a  -> Append
x  -> Create new file
b  -> Binary mode
t  -> Text mode (default)
+  -> Read & Write both
"""
