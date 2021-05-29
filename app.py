from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/Zeb')
def greet(name="Zeb"):
    return f"Hello {name}"


if __name__ == '__main__':
    app.run()
