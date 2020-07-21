$(function() {
    $('.cover_image').change(function(){
        const file = $(this)[0].files[0]
        const fileReader = new FileReader()
        const imageCoverSelect = document.querySelector('.image-cover-select');
        const imgCover = document.querySelector('.image-cover');

        if (file) {
            $('.image-cover').show();
            fileReader.readAsDataURL(file);
            imgCover.style.display = 'block';
            imageCoverSelect.innerHTML = 'Trocar imagem &nbsp;<i class="fa fa-image"></i>'
        } else {
            $('.image-cover').hide();
            imageCoverSelect.innerHTML = 'Selecionar capa da notícia &nbsp;<i class="fa fa-image"></i>'
        };

        fileReader.onloadend = function(){
            $('.image-cover').attr('src',fileReader.result);
        }
    });
});