$(function(){

    var model = {
        init: function() {
            if (!localStorage.cats) {
                localStorage.cats = JSON.stringify([]);
            }
        },
        add: function(obj) {
            var data = JSON.parse(localStorage.cats);
            data.push(obj);
            localStorage.cats = JSON.stringify(data);
        },
        getAllCats: function() {
            return JSON.parse(localStorage.cats);
        },
        populateCats: function() {
        	if (localStorage.cats.length < 5) {
	        	for (var i = 1; i<6 ; i++){
		        	model.add({
		        		id: i,
		        		name: 'cat' + i,
		        		clickCount: 0,
		        		img: 'http://placekitten.com/200/' + (i*100 + 300)
		        	});
		        }
		    }
        }
    };


    var octopus = {
        getCats: function() {
            return model.getAllCats();
        },

        // calls init function for both model and view and starts the page
        init: function() {
            model.init();
            catList.init();
            model.populateCats();
        }
    };


    var catList = {
        // create the functionality of the view page,
        // saves teh various aspects of the html to javascript variables
        // calls the appropriate functions when form submitted
        // adds the new note and clears the form after adding
        init: function() {
            this.buttonList = $('#cat-buttons');
            catList.render();
            catList.bindButtonToCats();
        },
        render: function(){
            var htmlStr = '';
            octopus.getCats().forEach(function(cat){
                htmlStr += '<button id="cat-button' + cat.id + '">' +
                        cat.name + '</button>';
            });
            this.buttonList.html( htmlStr );
        },
        bindButtonToCats: function() {
        	for (var i=1; i < 6; i++){
	            $('#cat-button' + i).click(function(e) {
		        	console.log(e.target.innerHTML); 
		        });
	        }
        }
    };

    octopus.init();
});