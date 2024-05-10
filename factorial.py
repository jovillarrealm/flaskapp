from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route("/<number>")
def hello_world(number):
    try:
        number = int(number)
    except ValueError:
        return "<p>NaN</p>"
    if isinstance(number, int):
        if number >= 0:
            fact = 1
            for i in range(number,0,-1):
                fact *= i
            return f"<p>{fact}</p>"
        else:
            return "<p>Número negativo</p>"
    return "<p>Hello</p>"