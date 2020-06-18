from flask import url_for

def url_for_notices(def_name, page, last_param = None):
    if def_name == 'notices':
        return url_for(def_name, page=page)
    if def_name == 'notices_by_game':
        return url_for(def_name, name=last_param, page=page)
