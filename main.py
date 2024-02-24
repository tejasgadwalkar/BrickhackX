import networkx as nx
import requests as rq
import graph
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():

    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
