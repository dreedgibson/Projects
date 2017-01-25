/*
 After you have changed the settings at "Your code goes here",
 run this with one of these options:
  "grunt" alone creates a new, completed images directory
  "grunt clean" removes the images directory
  "grunt responsive_images" re-processes images without removing the old ones
*/

module.exports = function(grunt) {

  grunt.initConfig({
    responsive_images: {
      dev: {
        options: {
          sizes: [{
            width: 200,
            suffix: "_2x",
            quality: 100
          },{
            width: 100,
            suffix: "_1x",
            quality: 100
          }],
        },

        /*
        All code for various picture gen here:
        main
        {
            width: 2400,
            suffix: "_large_2x",
            quality: 65
          },{
            width: 1200,
            suffix: "_large_1x",
            quality: 100
          },{
            width: 1600,
            suffix: "_med_2x",
            quality: 80
          },{
            width: 800,
            suffix: "_med_1x",
            quality: 100
          },{
            width: 800,
            suffix: "_sm_2x",
            quality: 100
          },{
            width: 400,
            suffix: "_sm_1x",
            quality: 100
          }]


        Apps
        {
            width: 700,
            suffix: "_2x",
            quality: 100
          },{
            width: 350,
            suffix: "_1x",
            quality: 100
          }]
        */


        /*
        You don't need to change this part if you don't change
        the directory structure.
        */
        files: [{
          expand: true,
          src: ['*.{gif,jpg,png,JPG}'],
          cwd: 'images_src/Logo/',
          dest: 'images/logo/'
        }]
      }
    },

    /* Clear out the images directory if it exists */
    clean: {
      dev: {
        src: ['images'],
      },
    },

    /* Generate the images directory if it is missing */
    mkdir: {
      dev: {
        options: {
          create: ['images']
        },
      },
    },

    /* Copy the "fixed" images that don't go through processing into the images/directory */
    copy: {
      dev: {
        files: [{
          expand: true,
          src: 'images_src/fixed/*.{gif,jpg,png}',
          dest: 'images/'
        }]
      },
    },
  });
  
  grunt.loadNpmTasks('grunt-responsive-images');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-mkdir');
  grunt.registerTask('default', ['clean', 'mkdir', 'copy', 'responsive_images']);

};
