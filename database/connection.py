from config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOSTNAME, MYSQL_DATABASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


def database_url():
    return "mysql+pymysql://%s:%s@%s/%s" % (
        MYSQL_USER,
        MYSQL_PASSWORD,
        MYSQL_HOSTNAME,
        MYSQL_DATABASE,
    )


# connection
engine = create_engine(database_url())
session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
session.configure(bind=engine)
db_session = scoped_session(session)

# mapping
base = declarative_base()  # 매핑선언
base.query = db_session.query_property()


def init_db():
    import app.main.models
    base.metadata.create_all(engine)

