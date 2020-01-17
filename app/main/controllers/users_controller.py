from flask import jsonify, Blueprint
from database.connection import init_db
from database.connection import session
from app.main.models import User


def api_users():
    print(User)

    users = session.query(User).filter(name='c')
    for user in users:
        print(user)

    return jsonify(dict(
        result=dict(
            # name=User.name,
            username='hello',
            # username=User.username
        )
    ))
