const baseUrl = window.location.href.toString()
const facebook = document.getElementById('facebook')
const twitter = document.getElementById('twitter')
const whatsapp = document.getElementById('whatsapp')

facebook.setAttribute('href', `https://www.facebook.com/sharer/sharer.php?u=${baseUrl}`)
twitter.setAttribute('href', `https://twitter.com/intent/tweet?url=${baseUrl}`)
whatsapp.setAttribute('href', `https://api.whatsapp.com/send?text=${baseUrl}`)
