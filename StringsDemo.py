str = "RahulShettyAcademy.com"
str1 = "Consulting Firm"
str3 = "RahulShetty"
str4 = " Trip "

print(str[1]) #a

print(str[0:5]) # for getting the Substring in python

print(str+" "+str1) # Concatenation

print(str3 in str) # Substring Check

# split
var = str.split(".")
print(var)
print(var[0])

# Trim - USed to remove the white spaces from the String
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())


