import address as ad
from flask import Flask, render_template, request, jsonify
import build_graph as bg

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


@app.route('/add_address', methods=['POST'])
def add_address():
    data = request.json
    address = data['address']
    addresses.append(address)
    return jsonify({'message': 'Address added successfully'})


@app.route('/get_addresses', methods=['GET'])
def get_addresses():
    return jsonify({'addresses': addresses})


@app.route('/delete_address', methods=['POST'])
def delete_address():
    data = request.json
    address = data['address']
    if address in addresses:
        addresses.remove(address)
        return jsonify({'message': 'Address deleted successfully'})
    else:
        return jsonify({'message': 'Address not found'})


@app.route('/build_path')
def build_path():
    mapGraph = bg.build_graph(addresses)
    return jsonify({'message': str(mapGraph)})


if __name__ == '__main__':
    app.run(debug=True)