const searchMobileInput = document.querySelector('.search-mobile-input');
const closerSearch = document.querySelector('.closer-search');
const searchMobileBody = document.querySelector('.search-mobile-body');
const searchMobileResults = document.querySelector('.search-mobile-results');
const write = document.querySelector('.write');
const searchButtonMobile = document.querySelector('#search-button-mobile');
const searchBackgroungMobile = document.querySelector('.search-background-mobile');

searchButtonMobile.addEventListener('click', () => {
    searchBackgroungMobile.style.display = 'block';
    searchMobileResults.style.left = '0px';
});

closerSearch.addEventListener('click', () => {
    searchBackgroungMobile.style.display = 'none';
    searchMobileResults.style.left = '-900px';
});

searchBackgroungMobile.addEventListener('click', () => {
    searchBackgroungMobile.style.display = 'none';
    searchMobileResults.style.left = '-900px';
});

searchMobileInput.addEventListener('input', () => {
    if (searchMobileInput.value === '' || searchMobileInput.value === '' || searchMobileInput.value === null) {
        searchMobileBody.innerHTML = '';
        write.innerHTML = 'Escreva para buscar';
    } else {
        let XHR = new XMLHttpRequest();
        XHR.open('GET', location.origin + `/search?q=${searchMobileInput.value}`, true);
        XHR.onreadystatechange = () => {
            if (XHR.readyState === 4) {
                if (XHR.status === 200) {
                    const allNews = JSON.parse(XHR.response)
                    let renderNews = '';

                    allNews.map((news) => {
                        let newsData = `
                            <div class="container">
                                <a href="${location.origin + '/news/' + news.id}">
                                    <div class="cover-image">
                                        <img src="${news.cover_image}" alt="">
                                    </div>
                                    <div class="data">
                                        <span class="title">${news.title}</span>
                                    </div>
                                </a>
                            </div>
                        `;

                        renderNews = renderNews + newsData;
                    });
                    searchMobileBody.innerHTML = ' ';
                    if (allNews.length === 0) {
                        write.innerHTML = `Nada foi encontrado para "${searchMobileInput.value}"`
                    };

                    if (allNews.length === 1) {
                        write.innerHTML = 'Resultado';
                    };

                    if (allNews.length > 1) {
                        write.innerHTML = 'Resultados';
                    };

                    if (searchMobileInput.value === '') {
                        write.innerHTML = 'Escreva para buscar';
                    };

                    searchMobileBody.innerHTML = renderNews;
                    searchMobileBody.style.animation = 'loadsItems 0.4s linear'
                };
            };
        };
        XHR.send();
    };
});
