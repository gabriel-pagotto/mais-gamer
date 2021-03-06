from app import app, database
from app.models import Users
from app.forms import LoginForm, RegisterForm
from app.utils.password_hash import set_password_hash, check_password_hash
from app.utils.font_control import lower, first_letter_upper
from flask import render_template, redirect, flash, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
    form = LoginForm()
    if form.validate_on_submit():
        username = Users.query.filter_by(username=form.username.data).first()
        if username is None or not check_password_hash(username.password, form.password.data):
            redirect(url_for('login'))
            flash('Nome de usuário ou senha inválidos.')
            username = form.username.data
            return render_template(
                'auth/login.html',
                title='Entrar',
                form=form,
            )
        login_user(username)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            return redirect(url_for('posts'))
        return redirect(next_page)
    return render_template(
        'pages/auth/login.html',
        title='Entrar',
        form=form,
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm_password.data:
            redirect(url_for('register'))
            flash('As senhas devem ser iguais.')
            username = form.username.data
            name = form.name.data
            surname = form.surname.data
            email = form.email.data
            return render_template(
                'auth/register.html',
                title='Criar conta',
                form=form,
            )
        user = Users(
            username=form.username.data,
            name=first_letter_upper(form.name.data),
            surname=first_letter_upper(form.surname.data),
            email=lower(form.email.data),
            password=set_password_hash(form.password.data),
        )
        database.session.add(user)
        database.session.commit()
        new_user = Users.query.filter_by(username=form.username.data).first()
        login_user(new_user)
        return redirect(url_for('posts'))

    return render_template(
        'pages/auth/register.html',
        title='Criar conta',
        form=form,
    )

@app.route('/auth/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
