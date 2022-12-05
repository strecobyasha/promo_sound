var lowerSlider = document.querySelector('#lower');
var upperSlider = document.querySelector('#upper');

upperSlider.oninput = function() {
    lowerVal = parseInt(lowerSlider.value);
    upperVal = parseInt(upperSlider.value);

    if (upperVal < lowerVal + 2) {
        lowerSlider.value = upperVal - 2;

        if (lowerVal == lowerSlider.min) {
            upperSlider.value = 2;
        }
    }
};

lowerSlider.oninput = function() {
    lowerVal = parseInt(lowerSlider.value);
    upperVal = parseInt(upperSlider.value);

    if (lowerVal > upperVal - 2) {
        upperSlider.value = lowerVal + 2;

        if (upperVal == upperSlider.max) {
            lowerSlider.value = parseInt(upperSlider.max) - 2;
        }
    }
};
