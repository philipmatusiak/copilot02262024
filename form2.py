# Using flask for a web framework, create the html code that accepts 4 inputs, first and last name, subtotal and tax as percentage, without using an html file. Add a button to the form that when submitted, returns subtotal, tax percentage and total on a new page. Calculate the total using a python function, called when the user click on the submit button. Using the re module in python, validate that the first and last name inputs do not contain numbers or special characters.

from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')

def index():
    return '''
    <form action="/result" method="post">
        <label for="first_name">First Name:</label><br>
        <input type="text" id="first_name" name="first_name"><br>
        <label for="last_name">Last Name:</label><br>
        <input type="text" id="last_name" name="last_name"><br>
        <label for="subtotal">Subtotal:</label><br>
        <input type="text" id="subtotal" name="subtotal"><br>
        <label for="tax">Tax Percent (Ex. 18):</label><br>
        <input type="text" id="tax" name="tax"><br><br>
        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/result', methods=['POST'])

def result():
    # if the return is asking the user to go back to the form, add a link to the form to go back
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    subtotal = request.form['subtotal']
    # using re module, validate that the subtotal input is a number
    if not re.search(r'[0-9]', subtotal):
        return f'Subtotal must be a number. Please go back and try again.'
    tax = request.form['tax']
    total = float(subtotal) + (float(subtotal) * (float(tax) / 100))
    if re.search(r'[0-9!@#$%^&*()_+=-]', first_name) or re.search(r'[0-9!@#$%^&*()_+=-]', last_name):
        return f'First and Last Name must not contain numbers or special characters. Please go back and try again.'   
    else:
        return f'First Name: {first_name}<br>Last Name: {last_name}<br>Subtotal: {subtotal}<br>Tax: {tax}%<br>Total: {total}'
    
if __name__ == '__main__':
    app.run(debug=True)

