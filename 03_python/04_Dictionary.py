#============= Dictionary ============

#----->> key:value pairs

#--> keys are always unique

# syntax
# my_dict = {key1: value1, key2: value2, key3: value3}

dict = {"name" : "Himanshu", "subject" : ["maths","science"],"score" : 97}

print(dict)

print(type(dict))

print(dict["name"]) # it's return the value that's index is given

#=========== dictionary are mutable and unordered ==================

dict = {"name" : "Himanshu", "subject" : ["maths","science"],"score" : 97}

dict["name"] = "Aman" # value will  be changed


print(dict)



#============== METHODS IN DICTONARY ==========

#d.keys() --> return all keys
#d.values() --> returmn all values
#d.items() --> return (key,val)pairs
#d.get(val) --> return val acc.to key
#d.update(new_item) --> adds new items to dict

dict = {"name" : "Himanshu", "subject" : ["maths","science"],"score" : 97}

print(dict.keys())

# dict[key] -->> val ---> if key is not exist then then it's give error value

# dict.get(key) -->> val ---> if key is not exist then it's give NONE value

dict = {"name" : "Himanshu", "subject" : ["maths","science"],"score" : 97}

print(dict.get("name2")) #wrong key -->> it's give None value

# print(dict.["name2"])        #wrong key -->> it's give error

dict.update({
    "city" : "Delhi"
})
# it's update the value 
print(dict)
