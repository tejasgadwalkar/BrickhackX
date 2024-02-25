import networkx as nx
import requests as rq
import graph
import address as ad
from flask import Flask, render_template, request
import json

app = Flask(__name__)
addresses = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        address_temp = request.form['address']
        address = ad.validate_address(address_temp)
        addresses.append(address)
        return render_template('index.html', addresses=addresses)
    return render_template('index.html', addresses=addresses)


@app.route('/locations', methods=['POST'])
def locations():
    loc1 = request.form['name']
    loc2 = request.form['email']
    return loc1 + loc2


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)
addresses = []

