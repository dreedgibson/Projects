var model = {
    attendance: function() {
        return JSON.parse(localStorage.attendance);
    },
    dayCount: 12,
    students: [
        {
            name: 'Slappy the Frog',
            daysMissed: 0
        },
        {
            name: 'Lilly the Lizard',
            daysMissed: 0
        },
        {
            name: 'Paulrus the Walrus',
            daysMissed: 0
        },
        {
            name: 'Gregory the Goat',
            daysMissed: 0
        },
        {
            name: 'Adam the Anaconda',
            daysMissed: 0
        }
    ]
};

/* STUDENTS IGNORE THIS FUNCTION
 * All this does is create an initial
 * attendance record if one is not found
 * within localStorage.
 */
(function randomChecks() {
    if (!localStorage.attendance) {
        console.log('Creating attendance records...');
        function getRandom() {
            return (Math.random() >= 0.5);
        }

        var students = model.students
        var attendance = {};

        students.forEach(function(o, i) {
            var name = students[i].name;
            attendance[name] = [];

            for (var i = 0; i < model.dayCount; i++) {
                attendance[name].push(getRandom());
            }
        });

        localStorage.attendance = JSON.stringify(attendance);
    }
}());

var controller = {
    $allMissed: $('tbody .missed-col'),
    $allCheckboxes: $('tbody input'),

    init: function() {
        view.init();
        controller.countMissing();
        view.updateTable();
    },

    getStudents: function() {
        return model.students;
    },

    numStudents: function() {
        return model.students.length;
    },
    // Count a student's missed days
    countMissing: function() {
        var students = controller.getStudents();
        for (var i = 0; i < controller.numStudents(); i++) {
            students[i].daysMissed = 0;
        }
        $('tbody .missed-col').each(function(i, v) {
            var studentRow = $(this).parent('tr'),
                dayChecks = $(studentRow).children('td').children('input'),
                numMissed = 0;
            dayChecks.each(function() {
                if (!$(this).prop('checked')) {
                    model.students[i].daysMissed++;
                }
            });
        });
    },

    getDayCount: function() {
        return model.dayCount;
    },

    getAttendance: function() {
        return model.attendance();
    },

    update: function() {
        var studentRows = $('tbody .student'),
            newAttendance = {};

        studentRows.each(function() {
            var name = $(this).children('.name-col').text(),
                $allCheckboxes = $(this).children('td').children('input');

            newAttendance[name] = [];

            $allCheckboxes.each(function() {
                newAttendance[name].push($(this).prop('checked'));
            });
        });

        controller.countMissing();
        localStorage.attendance = JSON.stringify(newAttendance);
        view.updateTable();
    }
};
var view = {
    init: function() {
        this.tableHead = $('#head');
        this.tableBody = $('#body');
        this.numStudents = controller.numStudents();
        this.numDays = controller.getDayCount(); 
        this.renderTable();
    },

    renderTable: function() {
        //build the table
        this.tableHead.append('<tr class="row"></tr>');
        $('.row:last').append('<th class="name-col">Student Name</th>');
        for (var i = 1; i <= this.numDays; i++) {
            $('.row:last').append('<th>' + i + '</th>');
        }
        $('.row:last').append('<th class="missed-col">Days Missed</th>');
        for (var i = 0; i < this.numStudents; i++){
            this.tableBody.append('<tr class="student"></tr>');
            $('.student:last').append('<td class="name-col"></td>');
            for(var j = 0; j < this.numDays; j++) {
                $('.student:last').append('<td class="attend-col"><input type="checkbox" onchange="controller.update()"></td>');
            }
            $('.student:last').append('<td class="missed-col"></td>');
        }

        // get the array of students and the hook for names
        var studentArr = controller.getStudents();
        this.studentNames = $('.name-col');
        for (var i = 1; i <= this.numStudents; i++) {
            this.studentNames[i].innerHTML = studentArr[i-1].name;
        }

        $.each(controller.getAttendance(), function(name, days) {
        var studentRow = $('tbody .name-col:contains("' + name + '")').parent('tr'),
            dayChecks = $(studentRow).children('.attend-col').children('input');

        dayChecks.each(function(i) {
            $(this).prop('checked', days[i]);
            });
        });
    },

    updateTable: function() {
        var students = controller.getStudents();
        this.studentMissed = $('.missed-col');
        for (var i = 1; i <= this.numStudents; i++) {
            this.studentMissed[i].innerHTML = students[i-1].daysMissed;
        }
    }
};
controller.init();
