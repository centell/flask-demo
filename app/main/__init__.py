from flask import Flask


def create_app(override=None):
    app = Flask(__name__)

    # initialize config (config.py)
    app.config.from_object('config')
    if override:
        app.config.update(override)

    @app.route('/')  # decorator 를 통해 라우팅 경로를 지정
    def hello_world():
        return 'Hello, World!'

    return app
