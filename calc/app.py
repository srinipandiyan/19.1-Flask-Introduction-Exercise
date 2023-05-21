from flask import Flask, request

from operations import *

app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to basic calculator"

@app.route('/add')
def show_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(add(a, b))
    return result

@app.route('/sub')
def show_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(sub(a, b))
    return result

@app.route('/mult')
def show_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(mult(a, b))
    return result

@app.route('/div')
def show_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(div(a, b))
    return result

##BONUS
operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route('/math/<operation>')
def general_math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(operators[operation](a, b))
    return result