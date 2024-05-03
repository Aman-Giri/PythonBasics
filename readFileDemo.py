file = open('test.txt')
# Read all the Contents of the file
# Read n number of the character by passing the parameter
# print(file.read(5))

# Read One single line at a time: readline()
# print(file.readline())
# print(file.readline())



# Print Line by line using the readline method
# line = file.readline()
# while line!= "":
#    print(line)
#    line = file.readline()


for line in file.readlines():
    print(line)


file.close()