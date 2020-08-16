const searchInput = document.querySelector('.search-input');
const containerResult = document.querySelector('.container-result');
const resultTitle = document.querySelector('.result-title');
const checkboxSearch = document.querySelector('.checkbox-search');
const backgroungSearch = document.querySelector('.background-search');

searchInput.addEventListener('input', () => {
    if (searchInput.value === '' || searchInput.value === '' || searchInput.value === null) {
        containerResult.innerHTML = '';
        resultTitle.innerHTML = 'Escreva para buscar';
    } else {
        let XHR = new XMLHttpRequest();
        XHR.open('GET', location.origin + `/buscar?q=${searchInput.value}`, true);
        XHR.onreadystatechange = () => {
            if (XHR.readyState === 4) {
                if (XHR.status === 200) {
                    const allNews = JSON.parse(XHR.response);
                    let renderNews = '';
                    allNews.map((news) => {
                        let newsData = `
                            <a href="${location.origin + '/notícia/' + news.id}">
                                <div class="container">
                                    <div class="cover_image">
                                        <img src="${news.cover_image}" alt="">
                                    </div>
                                    <div class="data">
                                        <span class="title">${news.title}</span>
                                        <span class="subtitle">${news.subtitle}</span>
                                    </div>
                                </div>
                            </a>
                        `;

                        renderNews = renderNews + newsData;
                    });
                    containerResult.innerHTML = ' ';
                    if (allNews.length === 0) {
                        resultTitle.innerHTML = `Nada foi encontrado para "${searchInput.value}"`
                    };

                    if (allNews.length === 1) {
                        resultTitle.innerHTML = 'Resultado';
                    };

                    if (allNews.length > 1) {
                        resultTitle.innerHTML = 'Resultados';
                    };
                    containerResult.innerHTML = renderNews;;

                    if (searchInput.value === '') {
                        resultTitle.innerHTML = 'Escreva para buscar';
                    };
                };
            };
        };
        XHR.send();
    };
});

searchInput.addEventListener('focus', () => {
    checkboxSearch.checked = true;
});

backgroungSearch.addEventListener('click', () => {
    checkboxSearch.checked = false;
});