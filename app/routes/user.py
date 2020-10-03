from app import app
from app.forms import ProfileForm
from flask import render_template
from flask_login import current_user, login_required


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    form.username.data = current_user.username
    form.name.data = current_user.name
    form.surname.data = current_user.surname
    form.email.data = current_user.email

    return render_template(
        'pages/profile.html',
        title=current_user.name,
        form=form,
    )
