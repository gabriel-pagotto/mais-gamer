const searchInput = document.querySelector('.search-input');
const containerResult = document.querySelector('.container-result');
const resultTitle = document.querySelector('.result-title');

searchInput.addEventListener('input', () => {

    if (searchInput.value === '' || searchInput.value === '' || searchInput.value === null ) {
        containerResult.innerHTML = '';
        resultTitle.innerHTML = 'Escreva para buscar'
    } else {
        let XHR = new XMLHttpRequest();
        XHR.open('GET', location.origin + `/buscar?q=${searchInput.value}`, true);
        XHR.onreadystatechange = () => {
            if (XHR.readyState === 4) {
                if (XHR.status === 200) {
                    const allNews = JSON.parse(XHR.response)
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
                    resultTitle.innerHTML = 'Resultados'
                    containerResult.innerHTML = renderNews;
                };
            };
        };
        XHR.send();
    };
});
