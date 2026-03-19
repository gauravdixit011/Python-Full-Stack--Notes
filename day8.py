# Set
# A Set stores unique elements.
items={1,2,3,3,4,5}
print(items)
# Duplicates are automatically removed
x=set() # blank set 
print(type(x))
# Unordered
# Unchangable
# Duplicate Not Allowed
fruits={"apple","banana","cherry"}

print(len(fruits)) # Get the Length of a Set

print("apple" in fruits)

# access item through the for loop
for fruit in fruits:
    print(fruit)

fruits.add("grapes") # add a single element
print(fruits)

fruits.update({"pineapple"}) # add multiple elements

print(fruits)

fruits.remove("cherry") # remove an item if the item remove not exist, 
#remove() raise an error 

print(fruits)

fruits.discard("cherry") # will not raise an error if item not exist

print(fruits)

# Remove a random item from the set
fruits.pop()

# Remove all items 
fruits.clear()

# delete fruits set variable
del fruits

# JOIN 

set1={"a","b","c"}
set2={1,2,3}

# UNION
set3=set1.union(set2)
# set3= set1 | set2
print(set3)

# INTERSECTION
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1.intersection(set2)
# set3= set1 & set2
print(set3)
# set1.intersection_update(set2)

# Difference
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}

set3=set1.difference(set2)
# set3=set1-set2
print(set3)
# set1.difference_update(set2) 

# Symmetric Difference
set3=set1.symmetric_difference(set2)
# set3 = set1 ^ set2
print(set3)
# set1.symmetric_difference_update(set2)

#  Dictionary
# A dictionary stores key-value pairs
student={
    "name":"Amit",
    "age":20,
    "course":"Python",
}

print(student)

print(student["name"]) # access the key's value

print(student.get("name"))  # access the key's value

print(student.keys()) # access all keys

print(student.values()) # access all values

print(student.items()) # access keys and values both


print("name" in student)

student["city"]="Lucknow" # add or Update
print(student)
print("city" in student)

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}

thisdict.update({"year":2026}) # add items

print(thisdict)

thisdict.pop("model") # remove the given item
print(thisdict)
thisdict.popitem() # removes the last inserted item
print(thisdict)

#del thisdict["model"]

thisdict.clear()


# Dictionary Problem
# 1. Create a dictionary called car with the keys
# "brand", "model","year" and values "Ford","Mustang",2026
# 2. Print the value of "model"  key
# 3. add a new key "color" with the value "red"
# 4. Remove the "brand" key using pop()
# 5. Print the Dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2026
}
print(car["model"])
car["color"] = "red"
car.pop("brand")
print(car)

# 1. Create a dictionary with keys: name, age , city
d={"name":"Raju","age":23,"City":"Noida"}
# 2. Access and print the value "name"
print(d["name"])
# 3. Add a new key "email" to a dictionary
d["email"]="raju@gmail.com"
#         or
# d.setdefault("email","raju@gmail.com")
print(d)
# 4. update the value of age
d=["age"]=26
# 5. delete a key "city"
del d["City"]