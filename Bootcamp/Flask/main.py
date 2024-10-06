# Flask is a framework
# Framework is a set of instruments that help developers create products 
# such as sites, apps, etc.
# Framework Flask creates web apps based on Python, HTML, CSS, JavaScript

from flask import Flask # from module import Class

app = Flask(__name__)   # Creating an instance of Flask class
# __name__ is the speical built-in variable that holds the name of the current module or script
# When a Python script is run directly, Python sets the value of __name__ to "__main__"
# When a script is imported as a module in another script or session, __name__ is set to the actual name of the module (app.py)

# Creating a decorator
@app.route('/') # GET - is the default method; '/' - URL path
def main():     # the view function that will be called when a user accesses this route
    return '<h1>Hello, world!</h1>'

@app.route('/info')
def info():
    return '<h1>I was created by GeekBrains</h1>'

@app.route('/sum/<x>/<y>')
def calculate(x, y):
    return f'<h1>{x} + {y} = {int(x) + int(y)}<h1>'

if __name__ == '__main__': # if the programm is launched from the main, not imported file (e.g app.py)
    app.run()              # then the app will run

