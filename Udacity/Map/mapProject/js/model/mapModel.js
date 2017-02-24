// model of individual locations
var Bar = function(data) {
	this.address = data.address;
	this.lat = data.lat;
	this.long = data.long;
	this.name = data.name;
	this.rating = data.rating;
	this.website = data.url;
}