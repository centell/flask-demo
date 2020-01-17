from flask import Flask, jsonify
import logging
import logging.handlers


def create_app(override=None):
    app = Flask(__name__)

    # initialize config (config.py)
    app.config.from_object('config')
    if override:
        app.config.update(override)

    # logging
    if not (app.config['DEBUG'] or app.config['TESTING']):
        handler = logging.handlers.RotatingFileHandler('/var/log/flask/flask.log')
        app.logger.addHandler(handler)

    # routers
    from app.main.controllers.users_controller import api_users
    @app.route('/')  # decorator 를 통해 라우팅 경로를 지정
    def hello_world():
        return str(app.config['ENV']) + '|' + str(app.config['DEBUG']) + '|' + str(app.config['TESTING'])
        # return 'Hello, World!'

    @app.route('/api/test')
    def api_test():
        return api_users()

    return app
