# Using flask for a web framework, create an html form that accepts 4 inputs, first and last name, subtotal and tax as percentage. Add a button to the form that when submitted, returns subtotal, tax percentage and total on a new page. Calculate the total using a python function, called when the user click on the submit button. Using the re module in python, validate that the first and last name inputs do not contain numbers or special characters.

from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form1.html')

@app.route('/result', methods=['POST'])

def result():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        subtotal = request.form['subtotal']
        tax = request.form['tax']
        total = float(subtotal) + (float(subtotal) * (float(tax) / 100))
        if re.search(r'\d', first_name) or re.search(r'\W', first_name) or re.search(r'\d', last_name) or re.search(r'\W', last_name):
            return render_template('form1.html', message='Invalid input. Name cannot contain numbers or special characters.')
        else:
            return render_template('result.html', first_name=first_name, last_name=last_name, subtotal=subtotal, tax=tax, total=total)
    return render_template('form1.html')

if __name__ == '__main__':
    app.run(debug=True)
