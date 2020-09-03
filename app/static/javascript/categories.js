const home = document.querySelector('.home');
const loadMoreButton = document.querySelector('.load-more');
const loads = document.querySelector('.loads');

let page = 0;
let totalPages = 0;
let working = false;
let animationTime = 0.7;

window.addEventListener('scroll', () => {
  const scrollCounter = (document.documentElement.scrollTop + window.innerHeight) >= document.documentElement.scrollHeight;
  if (scrollCounter === true && working === false) {
    if (totalPages === 0 || page < totalPages - 1) {
      loads.style.visibility = 'visible';
      working = true;
      page = page + 1;
      const xhr = new XMLHttpRequest;
      xhr.open('get', window.location + `?page=${page}`)
      xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            const data = response.pages;
            totalPages = response.total;
            const pageElement = document.createElement('div');
            pageElement.className = 'page';
            home.appendChild(pageElement);
            const headerArt = document.createElement('article');
            headerArt.className = 'header-art';
            headerArt.innerHTML = `
            <h3 class="header-title">
              <a href="${'/notícia/' + data.header.id}">${data.header.title}</a>
            </h3>
            <a href="${'/notícia/' + data.header.id}">
              <div class="header-pic">
                <img src="${data.header.cover_image}" alt="${data.header.title}">
              </div>
            </a>
            <p class="header-subtitle">
              <a href="${'/notícia/' + data.header.id}">${data.header.subtitle}</a>
            </p>
            <div class="infos">
              <a class="postedBy" href=""><i class="fas fa-user-tag">
              ${data.header.posted_by.name + ' ' + data.header.posted_by.surname}</i></a>
              <time datetime="${data.header.addedAt}"><i class="far fa-clock">
              ${data.header.datePost}</i></time>
            </div>
          `;
            pageElement.appendChild(headerArt);
            const restNotices = data.notices;
            for (counter = 0; counter < restNotices.length; counter++) {
              const element = data.notices[counter];
              const restArt = document.createElement('article');
              restArt.className = 'rest-art';
              restArt.innerHTML = `
              <a href="${'/notícia/' + element.id}">
                <div class="rest-pic">
                  <img src="${element.cover_image}" alt="${element.title}" title="${element.title}">
                </div>
              </a>
              <div class="infos">
                <h3 class="rest-title">
                  <a title="${element.title}" href="${'/notícia/' + element.id}">${element.title}</a>
                </h3>
                <p class="rest-subtitle">
                  <a href="${'/notícia/' + element.id}"> ${element.subtitle}</a>
                </p>
                <a class="postedBy" href=""><i class="fas fa-user-tag">
                  ${element.posted_by.name + ' ' + element.posted_by.surname}</i></a>
                <time datetime="${element.addedAt}"><i class="far fa-clock">
                  ${element.datePost}</i></time>
              </div>
            `;
              animationTime = animationTime + 0.2;
              const time = String(animationTime);
              restArt.style.animation = `loadsItems ${time}s  linear`
              pageElement.appendChild(restArt);
            };
            animationTime = 0.7;
            loads.style.visibility = 'hidden';
            working = false;
          };
        };
      };
      xhr.send();
    };
  };
});
