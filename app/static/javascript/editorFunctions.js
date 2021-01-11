const formSub = document.querySelector('.form-sub');
const editor = document.querySelector('.editor-container');
const contents = document.querySelector('.contents');
const editorOptions = document.querySelector('.editor-options');
const editorOptionsBackground = document.querySelector('.editor-options-background');
const postTitle = document.querySelector('.new-post-title');
const postSubtitle = document.querySelector('.new-post-subtitle');
const formGameID = document.querySelector('.select-game');
const isEsport = document.querySelector('.is-esport');
const sourceNameIn = document.querySelector('.source-name');
const sourceUrlIn = document.querySelector('.source-url');
const body = document.querySelector('body');
const imageCover = document.querySelector('.image-cover');
const error = document.querySelector('.error');
const category = document.querySelector('#category')

let counterPosition = 0;
let loadingCounter = 0;

const addTitle = document.querySelector('#add-title');
const addParagraph = document.querySelector('#add-paragraph');
const addImage = document.querySelector('#add-image');
const addCite = document.querySelector('#add-cite')
const addYoutubeVideo = document.querySelector('#add-youtube-video');
const addTwitterPost = document.querySelector('#add-twitter-post');
const remove = document.querySelector('#remove');

addTitle.addEventListener('click', () => {
  if (window.innerWidth > 1025) {
    hiddeOptions();
  };
  counterPosition = counterPosition + 1;
  const createdTitle = document.createElement('textarea');
  createdTitle.className = 'added-content';
  createdTitle.id = 'T';
  createdTitle.name = counterPosition;
  createdTitle.placeholder = 'Escreva o título';
  createdTitle.rows = '1';
  contents.appendChild(createdTitle);
  sizeTextAreas()
});

addParagraph.addEventListener('click', () => {
  if (window.innerWidth > 1025) {
    hiddeOptions();
  };
  counterPosition = counterPosition + 1;
  const createdTitle = document.createElement('textarea');
  createdTitle.className = 'added-content';
  createdTitle.id = 'P';
  createdTitle.name = counterPosition;
  createdTitle.placeholder = 'Escreva o paragrafo';
  createdTitle.rows = '1';
  contents.appendChild(createdTitle);
  sizeTextAreas()
});

addImage.addEventListener('click', () => {
  if (window.innerWidth > 1025) {
    hiddeOptions();
  };;
  const uploadFile = document.createElement('input');
  uploadFile.type = 'file';
  uploadFile.accept = 'images/*';
  uploadFile.style.display = 'none';
  contents.appendChild(uploadFile);
  uploadFile.click();

  const formData = new FormData();

  uploadFile.addEventListener('change', () => {
    const createdImage = document.createElement('img');
    createdImage.src = '/static/imageLoader.gif';
    createdImage.className = 'added-content';
    createdImage.id = 'IMG';
    contents.appendChild(createdImage);
    const XHR = new XMLHttpRequest;
    XHR.open('post', '/upload', true);
    XHR.onload
    XHR.onreadystatechange = () => {
      if (XHR.readyState === 4) {
        if (XHR.status === 200) {
          const data = JSON.parse(XHR.responseText);
          contents.removeChild(uploadFile);
          counterPosition = counterPosition + 1;
          createdImage.name = counterPosition;
          createdImage.src = data.url;
        };
      };
      uploadFile.removeEventListener('change', null);
    };
    formData.append('file', uploadFile.files[0]);
    XHR.send(formData)
  });
});

addCite.addEventListener('click', () => {
  if (window.innerWidth > 1025) {
    hiddeOptions();
  };
  counterPosition = counterPosition + 1;
  const createdTitle = document.createElement('textarea');
  createdTitle.className = 'added-content';
  createdTitle.id = 'C';
  createdTitle.name = counterPosition;
  createdTitle.placeholder = 'Escreva a citação';
  createdTitle.rows = '1';
  contents.appendChild(createdTitle);
  sizeTextAreas()
});

addYoutubeVideo.addEventListener('click', () => {
  if (window.innerWidth > 1025) {
    hiddeOptions();
  };
  const socialFinderContainer = document.createElement('div');
  socialFinderContainer.className = 'added-content'
  socialFinderContainer.id = 'social-finder-container';

  const socialFinderInput = document.createElement('input');
  socialFinderInput.type = 'url';
  socialFinderInput.placeholder = 'Coloque o link de compartilhamento do video do YouTube'
  socialFinderInput.className = 'socialFinderInput';

  const socialFinderButton = document.createElement('button');
  socialFinderButton.className = 'social-finder-button';
  socialFinderButton.id = 'inYTB';
  socialFinderButton.innerHTML = '<i class="fab fa-youtube"></i> Buscar'

  socialFinderContainer.appendChild(socialFinderInput);
  socialFinderContainer.appendChild(socialFinderButton);
  contents.appendChild(socialFinderContainer);

  socialFinderButton.addEventListener('click', () => {
    event.preventDefault();
    let value = socialFinderInput.value;
    value = value.split('.be/')
    if (value[0] === 'https://youtu') {
      contents.removeChild(socialFinderContainer);
      counterPosition = counterPosition + 1;
      const ytbVideo = document.createElement('iframe');
      ytbVideo.value = value[1];
      ytbVideo.className = 'added-content';
      ytbVideo.id = 'YTB';
      ytbVideo.name = counterPosition;
      ytbVideo.width = '100%';
      ytbVideo.height = '50vw';
      ytbVideo.src = `https://www.youtube.com/embed/${value[1]}`
      ytbVideo.frameborder = '0';
      ytbVideo.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
      ytbVideo.allowFullscreen = true;
      contents.appendChild(ytbVideo);
    } else {
      console.log('isWrong');
    };
  });
});

addTwitterPost.addEventListener('click', () => {
  if (window.innerWidth > 1025) {
    hiddeOptions();
  };
  const socialFinderContainer = document.createElement('div');
  socialFinderContainer.className = 'added-content'
  socialFinderContainer.id = 'social-finder-container';

  const socialFinderInput = document.createElement('input');
  socialFinderInput.type = 'text';
  socialFinderInput.placeholder = 'Coloque o código HTML da postagem do Twitter';
  socialFinderInput.className = 'socialFinderInput';

  const socialFinderButton = document.createElement('button');
  socialFinderButton.className = 'social-finder-button';
  socialFinderButton.id = 'inTWT';
  socialFinderButton.innerHTML = '<i class="fab fa-twitter"></i> Buscar'

  socialFinderContainer.appendChild(socialFinderInput);
  socialFinderContainer.appendChild(socialFinderButton);
  contents.appendChild(socialFinderContainer);

  socialFinderButton.addEventListener('click', () => {
    event.preventDefault();
    const code = socialFinderInput.value;
    const scriptTwt = document.createElement('script');
    scriptTwt.async = '';
    scriptTwt.src = 'https://platform.twitter.com/widgets.js';
    scriptTwt.charset = 'utf-8';
    contents.removeChild(socialFinderContainer);
    counterPosition = counterPosition + 1;
    const twtPost = document.createElement('div');
    twtPost.className = 'added-content';
    twtPost.id = 'TWT';
    twtPost.name = counterPosition;
    contents.appendChild(twtPost);
    twtPost.innerHTML = code;
    twtPost.value = code;
    twtPost.appendChild(scriptTwt);
  });
});

remove.addEventListener('click', () => {
  const addedContents = document.getElementsByClassName('added-content');
  if (addedContents.length >= 1) {
    contents.removeChild((addedContents[parseInt(addedContents.length) - 1]));
  }
});

formSub.addEventListener('submit', () => {
  event.preventDefault();
  const imageCover = document.querySelector('.image-cover');
  if (!imageCover.src) {
    return error.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Adicione uma capa para a notícia!'
  };

  if (imageCover.src === location.origin + '/static/imageLoader.gif') {
    return error.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Algumas imagens ainda estão carregando!'
  };

  loadingImages();

  if (loadingCounter > 0) {
    return error.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Algumas imagens ainda estão carregando!'
  };

  submit.innerHTML = '<i class="fas fa-spinner" id="submit-loads"></i> Enviando'
  submit.style.background = '#827189'
  submit.style.border = '1px solid #827189'
  submit.disabled = true;

  const addedContents = document.getElementsByClassName('added-content');

  let contents = [];

  for (x = 0; x < addedContents.length; x++) {
    const element = addedContents[x];
    if (element.id === 'T') {
      contents.push({
        type: 'T',
        position: element.name,
        data: {
          content: element.value,
          url: '',
        },
      });
    };

    if (element.id === 'P') {
      contents.push({
        type: 'P',
        position: element.name,
        data: {
          content: element.value,
          url: '',
        },
      });
    };

    if (element.id === 'C') {
      contents.push({
        type: 'C',
        position: element.name,
        data: {
          content: element.value,
          url: '',
        },
      });
    };

    if (element.id === 'IMG') {
      contents.push({
        type: 'IMG',
        position: element.name,
        data: {
          content: element.src,
          url: element.src,
        },
      });
    };

    if (element.id === 'YTB') {
      contents.push({
        type: 'YTB',
        position: element.name,
        data: {
          content: element.value,
          url: element.src,
        },
      });
    };

    if (element.id === 'TWT') {
      contents.push({
        type: 'TWT',
        position: element.name,
        data: {
          content: element.value,
          url: '',
        },
      });
    };
  };

  data = JSON.stringify({
    imageCover: imageCover.src,
    title: postTitle.value,
    subtitle: postSubtitle.value,
    contents: contents,
    category: category.value,
    source: {
      'name': sourceNameIn.value,
      'url': sourceUrlIn.value,
    },
  });

  const XHR = new XMLHttpRequest;

  XHR.open('post', '/posts/new')
  XHR.onreadystatechange = () => {
    if (XHR.readyState === 4) {
      if (XHR.status === 200) {
        const data = JSON.parse(XHR.responseText);
        if (data.status === 'success') {
          return window.open(data.redirect, '_blank');
        } else {
          console.log('error');
        };
        submit.innerHTML = '<i class="fas fa-spinner"></i> Enviando...'
        submit.style.background = '#ffa31a;'
        submit.style.border = '1px solid #ffa31a;'
        submit.disabled = false;
      };
    };
  };
  XHR.send(data);
});

editor.addEventListener('contextmenu', (e) => {
  if (window.innerWidth > 1025) {
    const x = (e.pageX - 3) + 'px';
    const y = (e.pageY - 2) + 'px';
    editorOptions.style.left = x;
    editorOptions.style.top = y;
    editorOptions.style.visibility = 'visible';
    editorOptionsBackground.style.visibility = 'visible';
  };
});

editorOptionsBackground.addEventListener('click', () => {
  if (window.innerWidth > 1025) {
    hiddeOptions();
  };
});

editorOptionsBackground.addEventListener('mouseover', () => {
  if (window.innerWidth > 1025) {
    hiddeOptions();
  };
});

function hiddeOptions() {
  editorOptions.style.visibility = 'hidden';
  editorOptionsBackground.style.visibility = 'hidden';
};

function orderInputs() {
  for (var i = 0; i < filhos.length; i++) {
    console.log(filhos[i]);
  }
};

function sizeTextAreas() {
  textAreas = document.getElementsByTagName('textarea');

  for (x = 0; x < textAreas.length; x++) {
    textAreas[x].addEventListener('input', function () {
      while (this.scrollHeight > this.offsetHeight) {
        this.rows += 1;
      }
    }
    )
  }
};

sizeTextAreas();

function loadingImages() {
  const addedContents = document.getElementsByClassName('added-content');
  loadingCounter = 0;
  for (x = 0; x < addedContents.length; x++) {
    const element = addedContents[x];
    if (element.src === location.origin + '/static/imageLoader.gif') {
      loadingCounter = loadingCounter + 1;
    };
  };

  if (loadingCounter > 0) {
    return;
  } else {
    loadingCounter = 0;
    error.innerHTML = '';
  };
};

setInterval(() => {
  if (window.innerWidth < 1025) {
    editorOptions.style.left = '0';
    editorOptions.style.top = 'auto';
    editorOptions.style.bottom = '0';
    editorOptions.style.visibility = 'visible';
  };
}, 1000);
