const noticeBody = document.querySelector('.notices-body');
const loadMoreButton = document.querySelector('.load-more');
const finalNotices = document.querySelector('.final-notices');

let page = 1;

function AJAX(urlExt, method) {
    const url = (location.href + urlExt)
    let XHR = new XMLHttpRequest();
    XHR.open(method, url, true);
    XHR.onreadystatechange = () => {
        if (XHR.readyState === 4) {
            if (XHR.status === 200) {
                totalPages = JSON.parse(XHR.responseText).total_pages;
                loadMoreButton.style.display = 'none';
                notices = JSON.parse(XHR.responseText).data;
                render = '';
                renderNotices = notices.map((notice) => {
                    renderData = `
                        <a href="${location.origin + '/notícia/' + notice.id}">
                            <div class="notice">
                                <div class="cover_image">
                                    <img src="${notice.cover_image}" alt="${notice.title}" class="cover_image">
                                </div>
                                <div class="notice-description">
                                    <h1 class="title">${notice.title}</h1>
                                    <h2 class="subtitle">${notice.subtitle}</h2>
                                    <div class="itens">
                                        <p class="addedAt"><i class="far fa-clock" style="margin-right: 5px;"></i>${notice.addedAt}</p>
                                    </div>
                                </div>
                            </div>
                        </a>
                    `
                    render = render + renderData;
                });
                noticeBody.innerHTML += `<div class="all-notices">${render}</div>`
                if (totalPages > page) {
                    setTimeout(() => {
                        loadMoreButton.style.display = 'block';
                    }, 500)
                };
                if (totalPages <= page) {
                    finalNotices.style.display = 'block';
                    loadMoreButton.style.display = 'none';
                    return
                };
            };
        };
    };
    XHR.send();
};

function loadMore() {
    page = page + 1;
    AJAX(`/páginação?page=${page}`, 'GET');
};
