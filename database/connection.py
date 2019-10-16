from sqlalchemy import create_engine
from config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOSTNAME, MYSQL_DATABASE


def database_url():
    return "mysql+pymysql://%s:%s@%s/%s" % (
        MYSQL_USER,
        MYSQL_PASSWORD,
        MYSQL_HOSTNAME,
        MYSQL_DATABASE,
    )


engine = create_engine(database_url())
