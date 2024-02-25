import address as ad
from flask import Flask, render_template, request, jsonify
import build_graph as bg
import shortest_path as sp

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



@app.route('/build_path', methods=['POST'])
def build_path():
    data = request.json
    starting_address = data.get('startingAddress')
    addresses = data.get('addresses', [])
    
    # Now you have both starting_address and addresses list
    # Use them to build the path
    builtGraph = bg.build_graph(addresses)
    optimized_path = sp.optimal_path(builtGraph, starting_address)
    print("starting address is: ", starting_address)
    print("optimization is: ", optimized_path)
    return jsonify({'path': optimized_path})


@app.route('/reset_addresses', methods=['POST'])
def reset_addresses():
    addresses.clear()
    return jsonify({'message': 'Addresses reset successfully'})


if __name__ == '__main__':
    app.run(host = "localhost", port="8123", debug=True)    