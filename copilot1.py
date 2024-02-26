# Create 2 variables for first name and last name, and join them together to create a full name

""" fname = "Bob"
lname = "Smith"
fullname = fname + " " + lname
print(fullname) """

# Ask the user to enter first, middle, last name and age, and print out the full name and age. Age needs to be an integer.

""" fname = input("Enter your first name: ")
mname = input("Enter your middle name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: ")) """

# Ask the user for their zipcode 
""" zipcode = input("Enter your zipcode: ") """

# Define a function that has 2 parameters called subtotal and tax rate. The subtotal and the tax rate will be entered by the user. When you call the function, pass the subtotal and tax rate as arguements to the function. Calculate the total amount, in the function, by adding the subtotal and the tax amount. The tax amount is calculated by multiplying the subtotal and the tax rate. Print out the total amount.

def calculate_total(subtotal, tax_rate):
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    print(total)
    # return total and then printing from the app

input_subtotal = float(input("Enter the subtotal: "))
input_tax_rate = float(input("Enter the tax rate: "))
calculate_total(input_subtotal, input_tax_rate)
