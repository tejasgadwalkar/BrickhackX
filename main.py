import networkx as nx
import requests as rq
import graph
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/locations', methods=['POST'])
def locations():
    loc1 = request.form['name']
    loc2 = request.form['email']
    return loc1 + loc2


if __name__ == '__main__':
    app.run(debug=True)
