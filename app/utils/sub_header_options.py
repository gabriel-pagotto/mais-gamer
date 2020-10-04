def sub_header(option_number, route_name):
    if route_name == 'posts':
        sub_header_options = {
            1: {
                'title': 'MINHAS POSTAGENS',
                'url': 'posts',
                'selected': False,
            },
            2: {
                'title': 'NOVA POSTAGEM',
                'url': 'post_new',
                'selected': False,
            },
        }

    elif route_name == 'groups':
        sub_header_options = {
            1: {
                'title': 'MEUS GRUPOS',
                'url': 'groups',
                'selected': False,
            },
            2: {
                'title': 'ADICIONAR UM GRUPO',
                'url': 'groups_new',
                'selected': False,
            },
        }

    sub_header_options[option_number]['selected'] = True
    options = []
    counter = 1
    while counter < len(sub_header_options) + 1:
        options.append(sub_header_options[counter])
        counter = counter + 1
    return options
