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
    listItem.innerHTML = address + ' <button onclick="deleteAddress(' + index + ')">Delete</button>';
    addressList.appendChild(listItem);
    addresses.push(address); // Add address to the addresses array

    // Update the starting address dropdown
    var startingAddressSelect = document.getElementById('startingAddress');
    var option = document.createElement('option');
    option.value = address;
    option.text = address;
    startingAddressSelect.add(option);
}

function deleteAddress(index) {
    var listItem = document.getElementById("address_" + index);
    var address = listItem.getAttribute('data-address');
    // Send request to server to delete address
    fetch('/delete_address', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({address: address})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        listItem.remove(); // Remove from webpage
    })
    .catch(error => console.error('Error:', error));
    listItem.remove(); // Remove from webpage

    // Update the starting address dropdown
    var startingAddressSelect = document.getElementById('startingAddress');
    for (var i = 0; i < startingAddressSelect.options.length; i++) {
        if (startingAddressSelect.options[i].value === address) {
            startingAddressSelect.remove(i);
            break;
        }
    }
}

function resetAddresses() {
    // Remove all addresses from the list and clear the array
    var addressList = document.getElementById('addressList');
    addressList.innerHTML = '';
    addresses = [];

    // Clear the starting address dropdown
    var startingAddressSelect = document.getElementById('startingAddress');
    startingAddressSelect.innerHTML = '';

    // Clear the displayed path on the map
    directionsDisplay.setMap(null);
}

function submitAddresses() {
//    clearMarkers()
    var startingAddress = document.getElementById('startingAddress').value;
    var waypoints = [];
    // Add the starting address as the first waypoint
    waypoints.push({
    location: startingAddress,
    stopover: true
    });
    // Add intermediate addresses as waypoints
    for (var i = 0; i < addresses.length - 1; i++) {
        waypoints.push({
            location: addresses[i],
            stopover: true
        });
    }

    var request = {
        origin: startingAddress,
        destination: addresses[addresses.length - 1],
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