from flask import Flask

app = Flask(__name__)


@app.route('/<string:name>')
def index(name):
    return "Hello, " + name


if __name__ == "__main__":
    app.run(debug='true')
