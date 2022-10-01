# mysql-test

## dockerでmysql環境を作成
```shell
docker image build -t mysql-1:latest . 
docker run --name mysql-1  -d -p 3306:3306 mysql-1
# CONTAINER ID を取得
docker ps

# CONTAINER IDとパスワードを保存
export CONTAINERID=<CONTAINER ID>
# Containerに接続
docker exec -it $CONTAINERID bash
```

```shell
# 再起動
docker start $CONTAINERID
# 停止
docker stop $CONTAINERID
```

## mysqlにログイン　パスワードは mysql
```bash
mysql -u root -p
```

## sql
### データベースを作成
```mysql
-- データベース python_test を作成
CREATE DATABASE python_test;
-- データベースの確認
SHOW DATABASES;

USE mydb;
SHOW TABLES;
SELECT * FROM table01;
```

## python3.7環境の作成
```shell
python3.7 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```