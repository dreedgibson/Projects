$(function(){

    var model = {
        init: function() {
            if (!localStorage.notes) {
                localStorage.notes = JSON.stringify([]);
            }
        },
        add: function(obj) {
            var data = JSON.parse(localStorage.notes);
            data.push(obj);
            localStorage.notes = JSON.stringify(data);
        },
        getAllNotes: function() {
            return JSON.parse(localStorage.notes);
        }
    };


    var octopus = {
        // adds a new note to the model taking in a parameter passed by the view
        addNewNote: function(noteStr) {
            model.add({
                content: noteStr,
                date: new Date(Date.now())
            });
            view.render();
        },

        getNotes: function() {
            return model.getAllNotes().reverse();
        },

        // calls init function for both model and view and starts the page
        init: function() {
            model.init();
            view.init();
        }
    };


    var view = {
        // create the functionality of the view page,
        // saves teh various aspects of the html to javascript variables
        // calls the appropriate functions when form submitted
        // adds the new note and clears the form after adding
        init: function() {
            this.noteList = $('#notes');
            var newNoteForm = $('#new-note-form');
            var newNoteContent = $('#new-note-content');
            newNoteForm.submit(function(e){
                octopus.addNewNote(newNoteContent.val());
                newNoteContent.val('');
                e.preventDefault();
            });
            view.render();
        },
        render: function(){
            var htmlStr = '';
            octopus.getNotes().forEach(function(note){
                htmlStr += '<li class="note">'+
                        note.content + '<span class="note-date">' + note.date +
                    '</span></li>';
            });
            this.noteList.html( htmlStr );
        }
    };

    octopus.init();
});