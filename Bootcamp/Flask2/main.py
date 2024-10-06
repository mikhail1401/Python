from flask import Flask

app = Flask(__name__)   # __name__ holds the name of the current module (main.py)

@app.route('/')
def main():
    return ''

if __name__ == '__main__':
    app.run()
