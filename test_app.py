from flask import Flask
from random import randint
from time import sleep

app = Flask(__name__)

@app.route("/")
def index():
    return "ok"

@app.route("/about")
def about():
    return "ok"

@app.route("/random")
def rndm():
    sleep(randint(0, 2))
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
