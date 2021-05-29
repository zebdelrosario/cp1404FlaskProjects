from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name="Zeb"):
    return f"Hello {name}"


@app.route('/Fahrenheit')
@app.route(f'/Fahrenheit/<float:celsius_temp>')
def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = celsius_temp * 9.0 / 5 + 32
    return str(fahrenheit_temp)


if __name__ == '__main__':
    app.run()
