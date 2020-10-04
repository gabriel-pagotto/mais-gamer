import requests
from app import app
from flask import render_template, jsonify, request
from flask_login import login_required
from app.utils.sub_header_options import sub_header
from bs4 import BeautifulSoup

@app.route('/groups', methods=['GET'])
@login_required
def groups():
    return render_template(
      'pages/groups/groups.html',
      title='Meus Grupos',
      sub_header=sub_header(1, 'groups'),
    )

@app.route('/groups/new', methods=['GET'])
@login_required
def groups_new():
    return render_template(
      'pages/groups/groups.html',
      title='Novo Grupo',
      sub_header=sub_header(2, 'groups'),
    )

@app.route('/groups/get-group-informations')
@login_required
def group_find_informations():
    url = request.args.get('url')

    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')

    name = soup.find('h2', class_='_2yzk').text

    icon = soup.find('span', class_='_2z9j')['style']
    icon = icon.split('(')
    icon = icon[1].split(')')
    icon = icon[0]

    return jsonify({
        'group': {
            'url': str(url),
            'name': str(name),
            'icon': str(icon),
        },
    })
