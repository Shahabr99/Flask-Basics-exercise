# Put your app in here.
from flask import Flask, request
from operations import *



app = Flask(__name__)

@app.route('/<operation>')
def calculate(operation):
  num1 = int(request.args.get('a'))
  num2 = int(request.args.get('b'))
 
  if operation == 'add':
    result = add(num1, num2)
  elif operation == 'subtract':
    result = sub(num1, num2)
  elif operation == 'division':
    result = div(num1, num2)
  elif operation == 'multiply':
    result = mult(num1, num2)
  else:
    return 'invalid operation'
  return str(result)
