// instanciando módulos
var gulp = require('gulp');
var watch = require('gulp-watch');
var del = require('del');
var shell = require('gulp-shell');
var connect = require('gulp-connect-multi')();

gulp.task('run:pelican', shell.task([
  'pelican content -s pelicanconf.py'
]));

gulp.task('clean:pelican', function () {
  return del([
    'output/*'
  ]);
});

gulp.task('connect', connect.server({
  root: ['output'],
  port: 1337,
  livereload: true,
  open: {
    browser: 'chrome' // if not working OS X browser: 'Google Chrome'
  }
}));

gulp.task('reload:output', function () {
  connect.reload();
});

gulp.task('watch', function(){
  gulp.watch('*', ['run:pelican', 'reload:output']);
  gulp.watch('content/*', ['run:pelican', 'reload:output']);
  gulp.watch('content/*/*', ['run:pelican', 'reload:output']);
  gulp.watch('content/*/*/*', ['run:pelican', 'reload:output']);
  gulp.watch('theme/*', ['run:pelican', 'reload:output']);
  gulp.watch('theme/*/*', ['run:pelican', 'reload:output']);
  gulp.watch('theme/*/*/*', ['run:pelican', 'reload:output']);
})

gulp.task('serve', ['connect', 'run:pelican', 'watch']);
