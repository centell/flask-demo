from alembic import command, config
from flask import Flask
import logging
import logging.handlers


def create_app(override=None):
    app = Flask(__name__)

    # initialize config (config.py)
    app.config.from_object('config')
    if override:
        app.config.update(override)

    # database connection

    # logging
    if not (app.config['DEBUG'] or app.config['TESTING']):
        handler = logging.handlers.RotatingFileHandler('/var/log/flask/flask.log')
        app.logger.addHandler(handler)

    @app.route('/')  # decorator 를 통해a 라우팅 경로를 지정
    def hello_world():
        return str(app.config['ENV']) + '|' + str(app.config['DEBUG']) + '|' + str(app.config['TESTING'])
        # return 'Hello, World!'
    return app
