var map;
var markers = [];
var addresses = []; // Array to store addresses
var directionsService;
var directionsDisplay;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 0, lng: 0},
        zoom: 2
    });

    directionsService = new google.maps.DirectionsService();
    directionsDisplay = new google.maps.DirectionsRenderer();
    directionsDisplay.setMap(map);

    map.addListener('click', function(event) {
        addMarker(event.latLng);
    });
}

function addMarker(location) {
    clearMarkers();
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
    markers.push(marker);
    document.getElementById('addressInput').value = getAddressFromLatLng(location);
}

function clearMarkers() {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(null);
    }
    markers = [];
}

function getAddressFromLatLng(latLng) {
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({'location': latLng}, function(results, status) {
        if (status === 'OK') {
            if (results[0]) {
                var address = results[0].formatted_address;
                document.getElementById('addressInput').value = address;
            }
        }
    });
}

function addAddress() {
    var address = document.getElementById('addressInput').value;
    var addressList = document.getElementById('addressList');
    var listItem = document.createElement('li');
    var index = addressList.getElementsByTagName("li").length + 1;
    listItem.id = "address_" + index;
    listItem.setAttribute('data-address', address);

    var counterWrapper = document.createElement('div');
    counterWrapper.id = "counter-wrapper";
    counterWrapper.innerHTML = '<label for="counter_' + index + '">No:</label>' +
                                '<input type="number" id="counter_' + index + '" name="counter_' + index + '" min="1" value="1">';

    var checkboxWrapper = document.createElement('div');
    checkboxWrapper.id = "checkbox-wrapper";
    checkboxWrapper.innerHTML = '<label for="checkbox_' + index + '">Pickup?</label>' +
                                 '<input type="checkbox" id="checkbox_' + index + '" name="checkbox_' + index + '">';

    listItem.innerHTML = address
    listItem.appendChild(counterWrapper);
    listItem.appendChild(checkboxWrapper);
    listItem.innerHTML += ' <button onclick="deleteAddress(' + index + ')">Delete</button>';
    addressList.appendChild(listItem);
    addresses.push(address); // Add address to the addresses array

    // Update the starting address dropdown
    var startingAddressSelect = document.getElementById('startingAddress');
    var option = document.createElement('option');
    option.value = address;
    option.text = address;
    startingAddressSelect.add(option);

    // Send the new address to the server for storage
    fetch('/add_address', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "address": address })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error('Error:', error));
}


function deleteAddress(index) {
    var listItem = document.getElementById("address_" + index);
    var address = listItem.getAttribute('data-address');

    // Remove from webpage
    listItem.remove();
    const tempindex = addresses.indexOf(address);
    if (tempindex > -1) { // only splice array when item is found
        addresses.splice(tempindex, 1); // 2nd parameter means remove one item only
    }

    // Remove from dropdown list
    var startingAddressSelect = document.getElementById('startingAddress');
    for (var i = 0; i < startingAddressSelect.options.length; i++) {
        if (startingAddressSelect.options[i].value === address) {
            startingAddressSelect.remove(i);
            break;
        }
    }

    // Send request to server to delete address
    fetch('/delete_address', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "address": address })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error('Error:', error));
}


function resetAddresses() {
    // Remove all addresses from the list and clear the array
    var addressList = document.getElementById('addressList');   
    addressList.innerHTML = '';
    addresses = [];
    clearMarkers()
    // Clear the starting address dropdown
    var startingAddressSelect = document.getElementById('startingAddress');
    startingAddressSelect.innerHTML = '';

    // Send request to server to reset addresses
    fetch('/reset_addresses', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error('Error:', error));
    // Clear the displayed path on the map
    initMap()
}


function submitAddresses() {
    var startingAddress = document.getElementById('startingAddress').value;
    if (!(addresses.includes(startingAddress))) {
        alert("Please select a valid starting address")
        return
    }

    // Prevent the default form submission behavior
    event.preventDefault();

    // print("addresses is : ", addresses)
    fetch('/build_path', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            'addresses': addresses,
            'startingAddress': startingAddress
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        displayOptimizedPath(data.path);  // Call a function to display the optimized path
    })
    .catch(error => console.error('Error:', error));
}

function displayOptimizedPath(optimizedPath) {
    var waypoints = [];

    // // Add the starting address as the first waypoint
    // waypoints.push({
    //     location: optimizedPath[0],
    //     stopover: true
    // });

    // Add intermediate addresses as waypoints
    for (var i = 0; i < optimizedPath.length; i++) {
        waypoints.push({
            location: optimizedPath[i],
            stopover: true
        });
    }

    var request = {
        origin: optimizedPath[0],
        destination: optimizedPath[optimizedPath.length - 1],
        waypoints: waypoints,
        travelMode: 'DRIVING'
    };

    directionsService.route(request, function(response, status) {
        if (status === 'OK') {
            directionsDisplay.setDirections(response);
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}
