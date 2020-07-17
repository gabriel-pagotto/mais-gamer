from flask import request

def notice_share(social_media):
    url = request.url
    if social_media.lower() == 'facebook':
        return ('https://www.facebook.com/sharer/sharer.php?u=' + url)
    elif social_media.lower() == 'twitter':
        return ('https://twitter.com/intent/tweet?url=' + url)
    elif social_media.lower() == 'whatsapp':
        return ('https://api.whatsapp.com/send?text=' + url)
