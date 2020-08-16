function AJAX(url, method) {
    let XHR = new XMLHttpRequest();

    XHR.open(method, url, true);
    XHR.onreadystatechange = () => {
        if (XHR.readyState === 4) {
            if (XHR.status === 200) {
                console.log('okay')
                return JSON.parse(XHR.responseText)
            };
        };
    };
    XHR.send();
};