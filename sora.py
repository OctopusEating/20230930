from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello everyone, my name is ”super man”"

@app.route("/sora")
def indox():
    return "What do you like subject?"

@app.route("/banana_cat")

def indx():
    return "It's good banana"

@app.route("/apple_dog")
def html():
    return render_template("banana.html")

app.run(host="0.0.0.0", port=5000)