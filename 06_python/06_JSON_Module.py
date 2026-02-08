# ========= JSON (JavaScript Object Notation) =========
"""
JSON is used to store and exchange data.

JSON  ->  Python
-----------------
object  -> dict
array   -> list
string  -> str
number  -> int / float
true    -> True
false   -> False
null    -> None
"""

import json


# -------- 1. json.loads() (JSON string → Python object) --------
print("----- json.loads() -----")

json_str = '{"name": "Himanshu", "isStudent": true}'

py_obj = json.loads(json_str)

print(type(py_obj), py_obj)
# Output: <class 'dict'> {'name': 'Himanshu', 'isStudent': True}


# -------- 2. json.dumps() (Python object → JSON string) --------
print("\n----- json.dumps() -----")

py_obj = {
    "name": "Aman",
    "isPolitician": True
}

json_str = json.dumps(py_obj)

print(type(json_str), json_str)
# Output: <class 'str'> {"name": "Aman", "isPolitician": true}


# -------- 3. json.load() (Read JSON file → Python object) --------
print("\n----- json.load() -----")

with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(type(py_obj), py_obj)


# -------- 4. json.dump() (Python object → JSON file) --------
print("\n----- json.dump() -----")

data = {
    "name": "Ramu",
    "age": 28,
    "isBandar": True
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
