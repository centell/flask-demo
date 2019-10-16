# FLASK DEMO

## Installed
```shell script
pip3 install flask
pip3 install requests  # https://realpython.com/python-requests/
pip3 install alembic  # https://alembic.sqlalchemy.org/en/latest/
pip install sqlalchemy-utils  # https://sqlalchemy-utils.readthedocs.io/en/latest/installation.html 
pip3 install -U python-dotenv  # https://pypi.org/project/python-dotenv
```

## Initialize
처음 프로젝트를 다운 받으면 다음을 실행합니다.
```shell script
source envirionment/init.sh
```

## Start database
테스트 데이터베이스는 `docker`로 구성된 `mariaDB`를 사용합니다.
```shell script
docker-compose up -d  # 도커로 데이터베이스 시작하기.
```

개인의 작업 환경에서 이미 3306 포트를 사용하고 있다면 `.env`에서 `MYSQL_PORT` 값을 수정하시면 됩니다.

## Alembic
### Create a Migration Script
`Alembic`은 데이터베이스 마이그레이션을 관리하는 도구입니다.  
이를 이용해 마이그레이션 스크립트를 생성합니다.
```shell script
alembic revision -m "create users table"
```
### Running Migration 
마이그레이션 스크립트를 실행하여 DB에 적용합니다.
```shell script
alembic upgrade head
```

## Start Project
```shell script
python3 run.py
```
