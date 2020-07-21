import os
from app import app
from app.models import Users, Posts, Games
from config import Config

debug = bool(os.environ.get('FLASK_DEBUG') == 'True')
port = int(os.environ.get('PORT', 7000))
context = 'adhoc'

if debug == True:
    app.run(host='0.0.0.0', port= port, debug=debug)
elif debug == False:
    app.run(host='0.0.0.0', port= port, debug=debug, ssl_context='adhoc')

@app.shell_context_processor
def make_shell_context():
    return {
        'database': database,
        'User': Users,
        'Post': Posts,
        'Game': Games,
    }
