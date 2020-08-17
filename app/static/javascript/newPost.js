const form = document.querySelector('.form-sub');
const submit = document.querySelector('.submit');
const selectEsports = document.querySelector('#select-esports');
const checkbox = document.querySelector('.is-esport');
const sourceQuestion = document.querySelector('#source-question');
const sourceName = document.querySelector('.source-name');
const sourceUrl = document.querySelector('.source-url');
const coverImageLabel = document.querySelector('.image-cover-select');

coverImageLabel.addEventListener('click', () => {
  event.preventDefault();
  const imageInput = document.createElement('input');
  imageInput.type = 'file';
  imageInput.style.display = 'none';
  form.appendChild(imageInput);
  imageInput.click();

  const XHR = new XMLHttpRequest();
  const formData = new FormData()

  imageInput.addEventListener('change', () => {
    XHR.open('post', '/upload', true);
    XHR.onload
    XHR.onreadystatechange = () => {
      if (XHR.readyState === 4) {
        if (XHR.status === 200) {
          form.removeChild(imageInput);
          const data = JSON.parse(XHR.responseText);
          const image = document.querySelector('.image-cover');
          image.style.display = 'block';
          coverImageLabel.innerHTML = 'Trocar imagem &nbsp;<i class="fas fa-exchange-alt"></i>';
          image.src = data.url;
        };
      };
    };
    formData.append('file', imageInput.files[0]);
    XHR.send(formData)
  });
});

checkbox.value = false;

sourceName.style.display = 'none';
sourceUrl.style.display = 'none';
sourceName.value = null;
sourceUrl.value = null;

sourceQuestion.addEventListener('change', () => {
  if (sourceQuestion.value === 'no') {
    sourceName.style.display = 'none';
    sourceUrl.style.display = 'none';
    sourceName.value = null;
    sourceUrl.value = null;
  } else {
    sourceName.style.display = 'block';
    sourceUrl.style.display = 'block';
  };
});

selectEsports.addEventListener('change', () => {
  if  (selectEsports.value === 'no') {
    checkbox.checked = false;
  } else {
    checkbox.checked = true;
  };
});

form.addEventListener('submit', () => {
    submit.value = 'Enviando'
    submit.style.background = '#827189'
    submit.style.border = '1px solid #827189'
});


$(function() {
    $('.cover_image').change(function(){
        const file = $(this)[0].files[0]
        const fileReader = new FileReader()
        const imageCoverSelect = document.querySelector('.image-cover-select');
        const imgCover = document.querySelector('.image-cover');

        if (file) {
            $('.image-cover').show();
            fileReader.readAsDataURL(file);
            imgCover.style.display = 'block';
            imageCoverSelect.innerHTML = 'Trocar imagem &nbsp;<i class="fas fa-exchange-alt"></i>'
        } else {
            $('.image-cover').hide();
            imageCoverSelect.innerHTML = 'Selecionar capa da notícia &nbsp;<i class="fa fa-image"></i>'
        };

        fileReader.onloadend = function(){
            $('.image-cover').attr('src',fileReader.result);
        }
    });
});
