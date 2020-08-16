from app import app, database
from app.models import Users, Posts, Games

debug = app.config['FLASK_DEBUG']
port = app.config['PORT']

app.run(host='0.0.0.0', port=port, debug=debug)


@app.shell_context_processor
def make_shell_context():
    return {
        'database': database,
        'User': Users,
        'Post': Posts,
        'Game': Games,
    }
