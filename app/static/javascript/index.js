const home = document.querySelector('.home');
const loadMoreButton = document.querySelector('.load-more');
const loads = document.querySelector('.loads');

let page = 0;
let totalPages = 0;
let working = false;
let animationTime = 0.7;

window.addEventListener('scroll', () => {
  const scrollCounter = (document.documentElement.scrollTop + window.innerHeight) >= document.documentElement.scrollHeight - 550;
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
            const headerArt = document.createElement('a');
            headerArt.className = 'header-art';
            headerArt.href = '/news/' + data.header.id;
            headerArt.innerHTML = `
              <div class="category">${ data.header.category.name }</div>
              <h3 class="header-title">${data.header.title}</h3>
              <div class="header-pic">
                <img src="${data.header.cover_image}" alt="${data.header.title}">
              </div>
              <p class="header-subtitle">${data.header.subtitle}</p>
              <div class="infos">
                <span class="postedBy"><i
                    class="fas fa-user-tag">${data.header.posted_by.name + ' ' + data.header.posted_by.surname}</i>
                </span>
                <time datetime="${data.header.addedAt}"><i class="far fa-clock">
                ${data.header.datePost}</i></time>
              </div>
            `;
            pageElement.appendChild(headerArt);
            const restNotices = data.notices;
            for (counter = 0; counter < restNotices.length; counter++) {
              const element = data.notices[counter];
              const restArt = document.createElement('a');
              restArt.className = 'rest-art';
              restArt.href = '/news/' + element.id;
              restArt.innerHTML = `
                <div class="rest-pic">
                  <img src="${element.cover_image}" alt="${element.title}">
                </div>
                <div class="infos">
                  <div class="category">${ element.category.name }</div>
                  <h3 class="rest-title">${element.title}</h3>
                  <p class="rest-subtitle">${element.subtitle}</p>
                  <span class="postedBy"><i
                      class="fas fa-user-tag">${element.posted_by.name + ' ' + element.posted_by.surname}</i></span>
                  <time datetime="${element.addedAt}"><i class="far fa-clock">
                    ${element.datePost}</i></time>
                </div>
              `;
              animationTime = animationTime + 0.2;
              const time = String(animationTime);
              restArt.style.animation = `loadsItems ${time}s  linear`
              pageElement.appendChild(restArt);

            };
            const scriptAd = document.createElement('script');
            scriptAd.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js';
            scriptAd.async = true;
            const adGoogle = document.createElement('div');
            adGoogle.appendChild(scriptAd);
            adGoogle.className = 'ad-h1';
            adGoogle.innerHTML += `
            <!-- H-1 -->
            <ins class="adsbygoogle"
                 style="display:block"
                 data-ad-client="ca-pub-1284323428666859"
                 data-ad-slot="8676887631"
                 data-ad-format="auto"
                 data-full-width-responsive="true"></ins>
            <script>
                 (adsbygoogle = window.adsbygoogle || []).push({});
            </script>
            `;
            pageElement.appendChild(adGoogle);
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
