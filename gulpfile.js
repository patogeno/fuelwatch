const { watch, src, dest, series } = require('gulp')
const uglify = require('gulp-uglifyjs')
const sass = require('gulp-sass')
const wait = require('gulp-wait')
const autoprefixer = require('gulp-autoprefixer')
const sourcemaps = require('gulp-sourcemaps')

function sassTask(cb) {
    return src('./dev/sass/**/*.scss')
        .pipe(wait(200))
        .pipe(sourcemaps.init())
            .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
            .pipe(autoprefixer('last 2 version', 'safari 5', 'ie 7', 'ie 8', 'ie 9', 'opera 12.1', 'ios 6', 'android 4'))
        .pipe(sourcemaps.write('./'))
        .pipe(dest('./static/css'))
    cb()
}

function uglifyTask(cb) {
    return src('./dev/js/**/*.js')
        .pipe(uglify('main.min.js'))
        .pipe(dest('./static/js'))
    cb()
}

exports.default = function() {
    watch('./dev/sass/**/*.scss', series(sassTask))
    watch('./dev/js/**/*.js', uglifyTask)
};

exports.build = series(sassTask, uglifyTask)
exports.sass = sassTask
