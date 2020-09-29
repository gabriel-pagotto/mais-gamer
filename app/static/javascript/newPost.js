const form = document.querySelector('.form-sub');
const submit = document.querySelector('.submit');
const sourceQuestion = document.querySelector('#source-question');
const sourceName = document.querySelector('.source-name');
const sourceUrl = document.querySelector('.source-url');
const coverImageLabel = document.querySelector('.image-cover-select');
const source = document.querySelector('.source');

coverImageLabel.addEventListener('click', () => {
  event.preventDefault();
  const imageInput = document.createElement('input');
  imageInput.type = 'file';
  imageInput.accept = 'images/*';
  imageInput.style.display = 'none';
  form.appendChild(imageInput);
  imageInput.click();

  const XHR = new XMLHttpRequest();
  const formData = new FormData()

  imageInput.addEventListener('change', () => {
    const image = document.querySelector('.image-cover');
    image.style.display = 'block';
    image.src = '/static/imageLoader.gif';
    XHR.open('post', '/upload', true);
    XHR.onload
    XHR.onreadystatechange = () => {
      if (XHR.readyState === 4) {
        if (XHR.status === 200) {
          form.removeChild(imageInput);
          const data = JSON.parse(XHR.responseText);
          image.style.display = 'block';
          image.src = data.url;
          coverImageLabel.innerHTML = 'Trocar imagem &nbsp;<i class="fas fa-exchange-alt"></i>';
        };
      };
    };
    formData.append('file', imageInput.files[0]);
    XHR.send(formData)
  });
});

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
    sourceUrl.style.display = 'block';
  };
});

sourceUrl.addEventListener('input', () => {
  sourceUrl.style.display = 'none';
  sourceName.style.display = 'none';

  const loader = document.querySelector('.source-loader');
  loader.style.display = 'block';

  const xhr = new XMLHttpRequest();

  xhr.open('post', '/get-site-informations');
  xhr.onload = () => {
    if (xhr.status != 200) {
      source.removeChild(loader);
      sourceUrl.style.display = 'block';
      sourceName.style.display = 'block';
      sourceName.value = null;
    };
    if (xhr.status === 200 && xhr.readyState === 4) {
      const response = JSON.parse(xhr.responseText);
      loader.style.display = 'none';
      sourceUrl.style.display = 'block';
      sourceUrl.value = response.site_url_origin;
      sourceName.style.display = 'block';
      sourceName.value = response.site_name;
    };
  };
  xhr.send(JSON.stringify({
    url: sourceUrl.value,
  }));
});
