var socket = io();
var lowerSlider = document.querySelector('#lower');
var upperSlider = document.querySelector('#upper');
var fadingStart = document.querySelector('#fading-start');
var fadingEnd = document.querySelector('#fading-end');
var file = document.querySelector('#file');


//function upload_sound() {
//    console.log('Try to upload sound...');
//    socket.emit('upload', 'data');
//}

//socket.on('message', data => {
//    for (const [key, value] of Object.entries(data)) {
//        el = document.getElementById(key);
//        el.innerHTML = value
//    };
//})

function start() {
    lowerVal = parseInt(lowerSlider.value);
    upperVal = parseInt(upperSlider.value);
    fadingStartVal = fadingStart.checked;
    fadingEndVal = fadingEnd.checked;

    console.log(
    "Sound will be cut in range " + lowerVal.toString() + " and " + upperVal.toString() + "; " +
    fadingStartVal + " " + fadingEndVal + " " + file.value
    )
    socket.emit('upload', file.value, lowerVal, upperVal);
}
