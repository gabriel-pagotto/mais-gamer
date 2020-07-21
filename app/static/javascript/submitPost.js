const form = document.querySelector('.form-sub');
const submit = document.querySelector('.submit');
form.addEventListener('submit', () => {
    submit.value = 'Enviando'
    submit.style.background = '#827189'
    submit.style.border = '1px solid #827189'
});
