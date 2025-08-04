from flask import Flask
app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello world</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://i.redd.it/an871k4o1sn51.png width=200">')

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye'

@app.route('/<name>/<int:age>')
def greet(name, age):
    return f"Hello {name}, you are {age} years old"

@app.route('/username/<path:name>')
def greet2(name):
    return f"Hi {name}"

if __name__ == "__main__":
    app.run(debug=True)