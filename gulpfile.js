var gulp = require('gulp');
var bundle = require('gulp-react-bundle');
 
gulp.task('build', function() {
  bundle('./app/static/js/Hello.jsx', './app/static/js/app.bundle.js');
});
 
gulp.task('build-with-dependency', function() {
  var lib = bundle.lib(['lodash', 'jquery'], './build/alpha.js');
  bundle('./js/app.js', './build/app.js', lib);
});
