var initialCats = [
        {
            clickCount : 0,
            name : 'Tabby',
            imgSrc : 'img/434164568_fea0ad4013_z.jpg',
            imgAttribution : 'https://www.flickr.com/photos/bigtallguy/434164568',
            nicknames: [
			{nickname: 'TabTab'},
			{nickname: 'T-bone'},
			{nickname: 'Mr. T'},
			{nickname: 'Tabby the Tab'}
		]
        },
        {
            clickCount : 0,
            name : 'Tiger',
            imgSrc : 'img/4154543904_6e2428c421_z.jpg',
            imgAttribution : 'https://www.flickr.com/photos/xshamx/4154543904',
            nicknames: [
			{nickname: 'TabTab'},
			{nickname: 'T-bone'},
			{nickname: 'Mr. T'},
			{nickname: 'Tabby the Tab'}
		]
        },
        {
            clickCount : 0,
            name : 'Scaredy',
            imgSrc : 'img/22252709_010df3379e_z.jpg',
            imgAttribution : 'https://www.flickr.com/photos/kpjas/22252709',
            nicknames: [
			{nickname: 'TabTab'},
			{nickname: 'T-bone'},
			{nickname: 'Mr. T'},
			{nickname: 'Tabby the Tab'}
		]
        },
        {
            clickCount : 0,
            name : 'Shadow',
            imgSrc : 'img/1413379559_412a540d29_z.jpg',
            imgAttribution : 'https://www.flickr.com/photos/malfet/1413379559',
            nicknames: [
			{nickname: 'TabTab'},
			{nickname: 'T-bone'},
			{nickname: 'Mr. T'},
			{nickname: 'Tabby the Tab'}
		]
        },
        {
            clickCount : 0,
            name : 'Sleepy',
            imgSrc : 'img/9648464288_2516b35537_z.jpg',
            imgAttribution : 'https://www.flickr.com/photos/onesharp/9648464288',
            nicknames: [
			{nickname: 'TabTab'},
			{nickname: 'T-bone'},
			{nickname: 'Mr. T'},
			{nickname: 'Tabby the Tab'}
		]
        }
    ]

var Cat = function(data) {
	this.clickCount = ko.observable(data.clickCount);
	this.name = ko.observable(data.name);
	this.imgSrc = ko.observable(data.imgSrc);

	this.level = ko.computed(function() {
		if (this.clickCount() < 10) {
			return 'Newborn';
		} else if (this.clickCount() < 25) {
			return 'infant';
		} else if (this.clickCount() < 50) {
			return 'child';
		} else {
			return 'teen';
		}
	}, this);

	this.nicknames = ko.observableArray(data.nicknames);
}

var ViewModel = function() {
	var self = this;

	this.catList = ko.observableArray([]);

	initialCats.forEach(function(catItem) {
		self.catList.push(new Cat(catItem));
	});

	this.currentCat = ko.observable(this.catList()[0]);
	this.incrementCounter = function() {
		this.clickCount(this.clickCount() + 1);
	}

	this.catUpdate = function(cat) {
		self.currentCat(cat);
	}	
};
ko.applyBindings(new ViewModel());