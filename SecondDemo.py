values = [1, 2, "Aman Giri", "Python", 44.5]
# List is the Data type that allows multiple values and can store different data types
# List is a mutable data type means we can change the existing values in it
print(values)
print(values[2])

# printing the last index of the list
print(values[-1])
print(values[1:3])

# insert between the list
values.insert(3,"Goswami")
print(values)

# appending in the list
values.append("Ending")
print(values)

# updating the values in the list
values[2] = "Giri ji"
print(values)

# deleting the values in the list
del values[0]
print(values)

# Tuples - Same as List Data type but immutable means we cannot change anything

val = (1, 2, "Aman", 7.8)
print(val[2])

#Dictionary:

dic = {"a": 2, 4: "Aman Giri", "c": "Goswami" }
print(dic["c"])

# Creating Dictionary at runTime only
dict = {}

dict["Firstname"] = "Rahul"
dict["Lastname"] = "Shetty"
dict["Gender"] = "Male"

print(dict)
print(dict["Firstname"])

