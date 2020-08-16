const inputs = document.getElementsByClassName('info-input');

function setInputsDisabled() {
    for (let counter = 0; counter < inputs.length; counter++) {
        inputs[counter].disabled = true;
    };
};

setInputsDisabled()