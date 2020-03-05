// instanciando módulos
var gulp = require('gulp');
var watch = require('gulp-watch');
var del = require('del');
var shell = require('gulp-shell');
var connect = require('gulp-connect');

gulp.task('run:pelican', shell.task([
  'pelican content -s pelicanconf.py'
]));

gulp.task('clean:pelican', function () {
  return del([
    'output/*'
  ]);
});

gulp.task('connect', function(){
  connect.server({
    root: ['output'],
    port: 1337,
    livereload: true
  });
});

gulp.task('reload:output', function () {
  connect.reload();
});

gulp.task('watch', function(){
  watch('*', gulp.series('run:pelican', 'reload:output'));
  watch('content/*', gulp.series('run:pelican', 'reload:output'));
  watch('content/*/*', gulp.series('run:pelican', 'reload:output'));
  watch('content/*/*/*', gulp.series('run:pelican', 'reload:output'));
  watch('theme/*', gulp.series('run:pelican', 'reload:output'));
  watch('theme/*/*', gulp.series('run:pelican', 'reload:output'));
  watch('theme/*/*/*', gulp.series('run:pelican', 'reload:output'));
})

gulp.task('serve', gulp.parallel('connect','run:pelican', 'watch'));
