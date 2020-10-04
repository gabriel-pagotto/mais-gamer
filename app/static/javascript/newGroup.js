const searchGroup = document.querySelector('.search-group');
const ngUrl = document.querySelector('.ng-url');
const ngSearch = document.querySelector('.ng-search');
const ngResult = document.querySelector('.ng-result');
const ngName = document.querySelector('.ng-name');
const ngIcon = document.querySelector('.ng-icon-img');

searchGroup.addEventListener('submit', searchGroupData);
ngResult.addEventListener('submit', sendGroup);

function sendGroup() {
  event.preventDefault();
};

function searchGroupData() {
  ngUrl.style.display = 'none';
  ngSearch.style.display = 'none';
  const sgLoader = document.querySelector('.sg-loader');
  sgLoader.style.display = 'block';
  event.preventDefault();
  const xhr = new XMLHttpRequest();

  xhr.open('get', `/groups/get-group-informations?url=${ngUrl.value}`);
  xhr.onload = () => {
    if (xhr.status === 200 && xhr.readyState ===4) {
      const response = JSON.parse(xhr.responseText);
      showNgResult(response.group);
    };
  };
  xhr.send();
};

function showNgResult(groupInformations) {
  searchGroup.style.display = 'none';
  ngResult.style.display = 'block';
  ngName.innerHTML = groupInformations.name;
  ngIcon.src = groupInformations.icon;
};
