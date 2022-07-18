import operations
from flask import request
from flask import Flask
app = Flask(__name__)


@app.route("/<operation>")
def calc(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    if operation == "add":
        return f"The addition is {operations.add(a, b)}"
    elif operation == "sub":
        return f"The difference is {operations.sub(a, b)}"
    elif operation == "mult":
        return f"The product is {operations.mult(a, b)}"
    elif operation == "div":
        return f"The quotient is {operations.div(a, b)}"


@app.route("/")
def init():
    return f"""<h1>You must use one of the following operations from the list and add the 'a' and 'b' values on the quesry string</h1>
        <ul>
        <li>add</li>
        <li>sub</li>
        <li>mult</li>
        <li>div</li>
        </ul>"""
