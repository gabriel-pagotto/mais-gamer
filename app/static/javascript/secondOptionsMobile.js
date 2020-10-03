const options1 = document.getElementById('options1');
const inputSecondOptionsMobile = document.getElementsByClassName('input-second-options-mobile');

function dockCloser() {
  for (let counter = 0; counter < inputSecondOptionsMobile.length; counter++) {
    if (options1.checked == false && inputSecondOptionsMobile[counter].checked == true) {
      inputSecondOptionsMobile[counter].checked = false
    };
  };
};
