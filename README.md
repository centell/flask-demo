# FLASK DEMO

## Installed
```shell script
pip3 install flask
pip3 install requests  # https://realpython.com/python-requests/
pip3 install alembic  # https://alembic.sqlalchemy.org/en/latest/
pip3 install -U python-dotenv  # https://pypi.org/project/python-dotenv
```

## Initialize
```shell script
source envirionment/init.sh
```

## start database
테스트 데이터베이스는 `docker`로 구성된 `mariaDB`를 사용합니다.
```shell script
docker-compose up -d  # 도커로 데이터베이스 시작하기.
```

개인의 작업 환경에서 이미 3306 포트를 사용하고 있다면 `.env`에서 `MYSQL_PORT` 값을 수정하시면 됩니다.

## Start Project
```shell script
python3 run.py
```
