from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')  # decorator 를 통해 라우팅 경로를 지정
    def hello_world():
        return 'Hello, World!'

    return app
