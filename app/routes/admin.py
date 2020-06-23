from app import app
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from app.utils.header_games import header_games
from app.utils.sub_header_options import sub_header

@app.route('/admin', methods=['GET'])
@login_required
def admin():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_admin != 1:
        return redirect(url_for('index'))


    return render_template(
        'admin/admin.html',
        title='Painel de administrador',
        header_games = header_games,
    )

@app.route('/admin/finances')
@login_required
def admin_finances():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_admin != 1:
        return redirect(url_for('index'))
    return 'Em breve...'

@app.route('/admin/notices')
@login_required
def admin_notices():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_admin != 1:
        return redirect(url_for('index'))
    return render_template(
        'admin/notices/notices.html',
        title = 'Notícias - Administrador',
    )

@app.route('/admin/social-media')
@login_required
def admin_social():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_admin != 1:
        return redirect(url_for('index'))
    return 'Em breve...'

@app.route('/admin/users')
@login_required
def admin_users():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_admin != 1:
        return redirect(url_for('index'))
    return 'Em breve...'