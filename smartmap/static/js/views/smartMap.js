$.shpn.SmartMap = Backbone.View.extend({
    locations: new $.shpn.LocationColaction(),
    markers: [],
    events: {
        "click .btn-reset": 'btnReset'
    },
    initialize: function () {
        var self = this;
        $.ajax({
            url: "https://maps.googleapis.com/maps/api/js",
            dataType: 'script',
            data: {
                'key': $.shpn.keyMapAPI,
                'callback': '$.shpn.initMap'
            }
        });

        $.shpn.initMap = function () {
            self.google = google;
            self.map = new self.google.maps.Map(document.getElementById('map'), {
                disableDoubleClickZoom: true,
                zoom: 13,
                center: {lat: -33.863, lng: 151.204},
                mapTypeId: 'terrain'
            });

            var geocoder = new google.maps.Geocoder;


            google.maps.event.addListener(self.map, 'click', function(event) {
                var marker = new google.maps.Marker({
                    position: event.latLng,
                    map: self.map
                });
                self.markers.push(marker);

                self.onMapClick(geocoder, event.latLng, marker);
            });
            self.showAllMarkers();
        };
        this.render();
    },
    render: function () {
        var self = this;

        self.$el.find('.location-list tbody').empty();
        while (self.markers.length > 0) {
           self.markers.pop().setMap(null);
        }

        this.locations.fetch({
            success: function (collection) {
                self.$el.find('.js-total-count').text(collection.size());
                collection.each(function(location) {
                    var locationView = new $.shpn.LocationView({model: location});
                    self.$el.find('.location-list tbody').append(locationView.render().el.childNodes);
                });
                self.showAllMarkers();
            }
        });
    },
    onMapClick: function geocodeLatLng(geocoder, latLng, marker) {
        var self = this;
        geocoder.geocode({'location': latLng}, function (results, status) {
            if (status === 'OK') {
                if (results[0]) {
                    var isAddress = false;
                    for(var result of results) {
                        if ($.inArray('street_address', result.types) > -1) {
                            self.notification('Yeh, this is a real address');
                            isAddress = true;

                            var location = new $.shpn.Location({
                                lat: latLng.lat(),
                                lng: latLng.lng(),
                                address: result.formatted_address
                            });

                            location.save(null, {
                                success: function () {
                                    self.render();
                                },
                                error:function(model, response){
                                    marker.setMap(null);
                                    self.notification(response);
                                }
                            });

                            break;
                        }
                    }
                }
            }

            if (!isAddress) {
                marker.setMap(null);
                self.notification('This is NOT a real address );');
            }
        });
    },
    showAllMarkers: function () {
        var self = this;
        if (!(self.google === undefined || self.google === null)) {
            self.locations.each(function(location) {
                var latLng = {
                        lat: parseFloat(location.get('lat')),
                        lng: parseFloat(location.get('lng'))
                    };
                var marker = new self.google.maps.Marker({
                    position: latLng,
                    map: self.map
                });
                self.markers.push(marker);
            });
        }
    },
    notification: function (text) {
        var self = this;
        var $notificator = self.$el.find('.js-notification');
        $notificator.text(text);
        setTimeout(function () {
            $notificator.text('');
        }, 1000);
    },
    btnReset: function () {
        var self = this;
        $.ajax({
            type: "DELETE",
            url: self.locations.url(),
            success: function(){
                self.render();
                self.notification('All data is reset')
            },
            error: function (msg) {
                self.notification('An error occurred: ' + msg);
            }
        });
    }
});
