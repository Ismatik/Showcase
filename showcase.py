#Showcase of the project using Django.
#Checking with github.

from concurrent.futures import thread
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1> Welcome, my daily task bot!<h1>"

if __name__ == "__main__":
    app.run(threaded = True)