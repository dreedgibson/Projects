// create global variables for use in map and marker functions.
var map;
var infoWindow;
var uluru = {lat: 39.7392, lng: -104.9903};

// create map
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: uluru,
        zoom: 14,
        mapTypeControl: false,
        styles: [
            {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
            {
                featureType: 'administrative.locality',
                elementType: 'labels.text.fill',
                stylers: [{color: '#d59563'}]
            },
            {
                featureType: 'poi',
                elementType: 'labels.text.fill',
                stylers: [{color: '#d59563'}]
            },
            {
                featureType: 'poi.park',
                elementType: 'geometry',
                stylers: [{color: '#263c3f'}]
            },
            {
                featureType: 'poi.park',
                elementType: 'labels.text.fill',
                stylers: [{color: '#6b9a76'}]
            },
            {
                featureType: 'road',
                elementType: 'geometry',
                stylers: [{color: '#38414e'}]
            },
            {
                featureType: 'road',
                elementType: 'geometry.stroke',
                stylers: [{color: '#212a37'}]
            },
            {
                featureType: 'road',
                elementType: 'labels.text.fill',
                stylers: [{color: '#9ca5b3'}]
            },
            {
                featureType: 'road.highway',
                elementType: 'geometry',
                stylers: [{color: '#746855'}]
            },
            {
                featureType: 'road.highway',
                elementType: 'geometry.stroke',
                stylers: [{color: '#1f2835'}]
            },
            {
                featureType: 'road.highway',
                elementType: 'labels.text.fill',
                stylers: [{color: '#f3d19c'}]
            },
            {
                featureType: 'transit',
                elementType: 'geometry',
                stylers: [{color: '#2f3948'}]
            },
            {
                featureType: 'transit.station',
                elementType: 'labels.text.fill',
                stylers: [{color: '#d59563'}]
            },
            {
                featureType: 'water',
                elementType: 'geometry',
                stylers: [{color: '#17263c'}]
            },
            {
                featureType: 'water',
                elementType: 'labels.text.fill',
                stylers: [{color: '#515c6d'}]
            },
            {
                featureType: 'water',
                elementType: 'labels.text.stroke',
                stylers: [{color: '#17263c'}]
            }
        ]
    });
    infoWindow = new google.maps.InfoWindow;
}

// build initialPlaces Array
var initialPlaces;

// foursquare api is used to retrieve the initial list of data
function initialList() {
    // build url to get bars around Denver, CO from Foursquare
    var url = 'https://api.foursquare.com/v2/venues/explore?';
    url += $.param({
        near: 'Denver, CO',
        query: 'bars',
        limit: '40',
        v: '20161016',
        radius: '3000',
        client_id: 'OD1J1MST4OIUBTB44K54Q2SM0XP2WOWVYL5DXQB1NHGHAQNW',
        client_secret: 'NZ3UEOUA3OI3WICXMUA3UZGKJXF5RYZMI2RDSR3F2NZGSJXL'
    });

    return $.ajax({
        dataType: "json",
        url: url,
        success: function(data) {
            initialPlaces = data.response.groups[0].items;
        }
    }).fail(function(e) {
        alert('Failed to retrieve data from Foursquare.');
    });
}

function googleError() {
    alert('Failed to load Google Maps');
}

var myViewModel = function() {
    // create self variable for use in lower level data binds
    var self = this;

    // obervable array of markers
    this.markers = ko.observableArray([]);

    // create observable for input value:
    this.filterValue = ko.observable();

    // observable array of locations
    this.locationsList = ko.observableArray([]);

    // Array for filtered locations
    this.filteredLocations = ko.observableArray([]);
    this.filteredLocations(null);

    // sidebar width
    this.sidebarWidth = ko.observable('20%');

    // hamburger margin
    this.hamMargin = ko.observable('20%');

    // build locations list array when initial list ajax has finished.
    $.when(initialList()).done(function() {
        initialPlaces.forEach(function(item) {
            var data = {
                address: item.venue.location.address + ' ' + item.venue.location.city,
                lat: item.venue.location.lat || 'no Latitude Coordinate',
                long: item.venue.location.lng || 'no Long Coordinate',
                name: item.venue.name || 'no Name Provided',
                rating: item.venue.rating || 'No Rating Yet',
                url: item.venue.url || 'No Website Provided'
            };
            self.locationsList.push(new Bar(data));
        });

        // place initial markers on map
        self.locationsList().forEach(function(bar) {
            self.createMarkers(bar);
        });
    });

    // function to create markers on map
    // these functions were taken from google documentation in order to work with markers
    this.createMarkers = function(bar) {
        var marker = new google.maps.Marker({
            position: {lat: bar.lat, lng: bar.long},
            map: map,
            animation: google.maps.Animation.DROP,
            // credit Maps Icons Collection
            icon: 'img/bar.png'
        });

        // add event listener to toggle the bounce feature and the open window
        marker.addListener('click', function() {
            self.toggleBounce(marker);
            self.openInfoWindow(marker);
        });
        self.markers().push(marker);
    };

    // create the bounce animation and have the pin bounce once and stop
    this.toggleBounce = function(marker) {
        if (marker.getAnimation() !== null) {
            marker.setAnimation(null);
        } else {
            marker.setAnimation(google.maps.Animation.BOUNCE);
            window.setTimeout(function() {
                marker.setAnimation(null);
            }, 700);
            console.log(self.markers()[2]);
        }
    };

    // open an info window on the clicked marker
    this.openInfoWindow = function(marker) {
        var barSelect;
        // find the bar that was clicked from array
        if (self.filteredLocations() !== null && self.filteredLocations().length > 0) {
            self.filteredLocations().forEach(function(bar) {
                if (bar.lat === marker.position.lat()) {
                    barSelect = bar;
                }
            });
        } else {
            self.locationsList().forEach(function(bar) {
                if (bar.lat === marker.position.lat()) {
                    barSelect = bar;
                }
            });
        }

        // create content string
        var contentString = '<div class="iw-container">' + '<h4 class="iw-title">' + barSelect.name + '</h4>' +
                '<p class="i-content">Address: ' + barSelect.address + '</p>' +
                '<p class="i-content">Website: ' + barSelect.website + '</p>' +
                '<p class="i-content">Rating: ' + barSelect.rating + '</p></div>'

        // create infoWindow
        infoWindow.setContent(contentString);

        // open the infoWindow
        infoWindow.open(map,marker);
    };

    // clear markers
    this.clearMarkers = function() {
        for (var i = 0; i < self.markers().length; i++) {
            self.markers()[i].setVisible(false);
        }
    };

    // subscribe to filterValue to update the filtered list every input character
    self.filterValue.subscribe(function(c) {
        // if length of filterValue is 0 set filteredLocations to null and create markers for locationsList
        if (c.length === 0) {
            // set the filteredLocations variable to null
            self.filteredLocations(null);
            // set all markers visible
            self.markers().forEach(function(marker) {
                marker.setVisible(true);
            });
        } else {
            // Clear markers from map
            self.clearMarkers();
            // create the filteredLocations array
            self.filteredLocations([]);
            // push the values into the filtered array
            self.locationsList().forEach(function(bar) {
                if (bar.name.toLowerCase().includes(c.toLowerCase())) {
                    self.filteredLocations.push(bar);
                }
            });
            // set only filtered markers visible
            self.filteredLocations().forEach(function(bar) {
                self.markers().forEach(function(marker) {
                    if (marker.position.lat() === bar.lat) {
                        marker.setVisible(true);
                    }
                });
            });
        }
    });

    // handler for clicking on list item to bring up associated marker
    this.listClickHandler = function(item) {
        var markerSelect;
        console.log(item);
        self.markers().forEach(function(marker) {
            console.log(marker);
            if (marker.position.lat() === item.lat) {
                markerSelect = marker;
            }
        });
        self.toggleBounce(markerSelect);
        self.openInfoWindow(markerSelect);
    };

    // toggle the sidebar to be 20% of screen width
    this.toggleSidebar = function() {
        if (self.sidebarWidth() === 0) {
            self.sidebarWidth('20%');
            self.hamMargin('20%');
        } else {
            self.sidebarWidth(0);
            self.hamMargin('20px');
        }
    }
    console.log(self.filteredLocations())
};
ko.applyBindings(new myViewModel());