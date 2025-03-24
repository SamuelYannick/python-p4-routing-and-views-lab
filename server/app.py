#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:strParam>')
def print_string(strParam):
    print(strParam)
    return strParam

@app.route('/count/<int:param>')
def count(param):
    result = ""
    for i in range(param):
        result += f"{i}\n"
    return result

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    print("Select operation: +, -, * or div")
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div" and num2 != 0:
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation!"
    
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
