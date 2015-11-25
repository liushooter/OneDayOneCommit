module.exports = (grunt) ->
  config = {
    path: "./common/static/js"
    dist: "./common/static/release"
    brower_path: "./components/bower_components"
  }
  #
  grunt.initConfig({
    pkg: grunt.file.readJSON('./package.json'),
    config: config,

    concat: {
      options: {
        separator: ';'
        # stripBanners: true
      },
      js: {
        src: ["<%= config.path %>/**/*.js"]
        dest: "<%= config.dist %>/js/app.js"
      }
    },
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      compress: {
        options: {
           mangle: true
        },
        files: [{
            expand: true
            src: '<%= config.dist %>/js/app.js'
            dest: './'
            ext: '.min.js'
        }]
      }
    }
  #
  })

  grunt.loadNpmTasks('grunt-contrib-clean')
  grunt.loadNpmTasks('grunt-contrib-concat')
  grunt.loadNpmTasks('grunt-contrib-cssmin')
  grunt.loadNpmTasks('grunt-contrib-uglify')
  # grunt.loadNpmTasks('grunt-contrib-watch')
  grunt.loadNpmTasks('grunt-contrib-connect')
  # grunt.loadNpmTasks('grunt-karma');

  grunt.registerTask('default', ['concat', 'uglify'])
