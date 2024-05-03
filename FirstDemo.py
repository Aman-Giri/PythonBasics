print("Hello World")
# here are the comments I have defined
a = 3
print(a)
b = "Aman Giri"
print(b)

c, d, e = 23, 23.5, "Greatt"
# print("Value is" + b) It will give error

print("{}{}".format("the value of c is: ", c))

print("{} {}".format("Value is", d))
print(type(a))
print("{} {}".format("The data type of a is", type(a)))
print("{} {}".format("The data type of a is", type(d)))
print("{} {}".format("The data type of a is", type(e)))

# Concatenation works only for the same data types
print(b+" concatenate with "+e)
