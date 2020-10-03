from app import app
from flask import render_template
from flask_login import login_required

@app.route('/groups', methods=['GET'])
@login_required
def groups():
    return 'okay'
