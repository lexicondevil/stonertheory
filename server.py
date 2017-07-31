from flask import Flask
from flask import render_template

app = Flask(__name__)

x = 'They don’t mind you struggling for freedom as long as you struggle according to their rules.\n\n As long as you let them tell you how to struggle, they go for your struggle.\n But as soon as you come to one of them who is supposed to be for your freedom and tell him you’re for freedom by any means necessary, he gets away from you.\n He’s for his freedom by any means necessary, but he’ll never go along with you to get your freedom by any means necessary.'

@app.route("/")
def hi():
    return x

