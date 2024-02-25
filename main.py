import address as ad
from flask import Flask, render_template, request, jsonify
import graph

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
    address = data["address"]
    if address in addresses:
        print("removed address should been: ", address)
        addresses.remove(address)
        print("addressing from main is: ", addresses)
        return jsonify({'message': 'Address deleted successfully'})
    else:
        return jsonify({'message': 'Address not found'})



@app.route('/build_path', methods=['POST'])
def build_path():
    data = request.json
    starting_address = data.get('startingAddress')
    ending_address = data.get('endingAddress') #potentially none
    assert(starting_address is not None)
    addresses = data.get('addresses')
    
    # print("addresses is: ", addresses)

    if (ending_address == None):
        optimized_path = graph.generate_optimal_path(addresses, starting_address)
    else:
        optimized_path = graph.generate_optimal_path(addresses, starting_address, ending_address)
    # print("starting address is: ", starting_address)
    # print("optimization is: ", optimized_path)
    return jsonify({'path': optimized_path})


@app.route('/reset_addresses', methods=['POST'])
def reset_addresses():
    addresses.clear()
    return jsonify({'message': 'Addresses reset successfully'})


if __name__ == '__main__':
    app.run(host = "localhost", port="8123", debug=True)    