'''
Multi Line 
or block comment
'''
# Line Comment or using to prompt Github Copilot

# 3.1.1 page 9
x = 7
y = '3'  # y is var name and string is the data type
z = x + int(y)     # cast y as int   
print(z)   # Assert 10  

# Create a formula to add two int varibles, x and y, then print them as z
'''
x,y = 7,3
z = x + y
print(z)
'''
'''
x = 7
y = 3
print(x + y)
'''
# Using python, create three int variables named x,y,z. Ask the user to input x and y as casted integers using input(), then add the user input to z and use the print() to output the result. Be as pythonic in the code as possible and parameterize all string functions instead of using joins.

# 3.1.2 Strings page 11 - 14
# 1. join + data type
# 2. parameter , !type
fname = "Bob"
lname = 'Smith'
age = 42
fullinfo  = fname + ' ' + lname + ' ' + str(age) 
fullinfoparam = 'First name: ',fname,'Last Name: ',lname,'Age: ', age
print(fullinfo)
print(fullinfoparam)

# 3.1.3 Lists page 14 AND other collection types
'''
List [element , element] indexed, single, !sorted, dups, mutable page 14
Sets {item, item, ...} !indexed, !stored, immutable, single, !dups
Tuples (params, params,...) Most secure, indexed, dups, immutable, single
Map/Dict {key:value, key:value, ...} key!dup, valuedups
'''
fnames = ['Bob','Mary','Joe'] # List of fnames len(3) range[0:2]
print(fnames)

'''
for x in ys
x local variable in the scope
ys where is the data coming from
4.2 page 19
'''
for fname in fnames:
    print("Contact first name: " + fname) # param , join + 

# Loop thru the fnames list and print each contact. Use the for loop and define the local variable as fname. Add a string "Contact first name: " at the beginning of the print(), and use a join operator, instead of parameterizing the print()
    
# 4.8 Functions page 27  (method / return)
# define a function that adds x and y as z and print(z)
# call a function  

def myCalc():
    x,y = 7,3
    z = x + y
    print(z)

myCalc()

# defining the functions
def myCalc1(x,y):  # params
    z = x + y
    print(z)

# calling the function
myCalc1(7,3) # args passing then to the param

# get the inputs from a user input()
x1 = input("Enter the value for x: ")  # int()
y1 = input("Enter the value for y: ")  # int()

def myCalc2(x1, y1):
    z = int(x1) + int(y1)
    print(z)

myCalc2(x1, y1)

