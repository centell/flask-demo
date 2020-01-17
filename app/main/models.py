from database.connection import base
from sqlalchemy import Column, INTEGER, VARCHAR, CHAR


class User(base):
    __bind_key__ = 'default'
    __tablename__ = 'users'
    __table_args__ = dict(
        mysql_engine='InnoDB',
        mysql_row_format='DYNAMIC',
        mysql_charset='utf8mb4',
        mysql_collate='utf8mb4_unicode_ci'
    )

    id = Column(INTEGER, primary_key=True)
    username = Column(VARCHAR(100), nullable=False)
    password = Column(CHAR(41), nullable=True)
    name = Column(VARCHAR(30), nullable=False)

    def __init__(self, name, fullname, password):
        self.name = name
        self.username = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.username, self.password)
