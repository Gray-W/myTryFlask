# -*-coding:unicode_escape-*-
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_world():
    return "Hello, World!"


@app.route('/', methods=["POST"])
def helloworld():
    return "POST METHOD Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)