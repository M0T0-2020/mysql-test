# mysql-test

## dockerでmysql環境を作成し、コンテナ内に移動
```shell
sh DockerBuildStart.sh
```

```shell
# 再起動
docker start $(docker ps -q | head -1)
# 停止
docker stop $(docker ps -q | head -1)
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

-- テーブルの作成
DROP DATABASE IF EXISTS mydb;
create database mydb;
USE mydb;
create table table01(col1 int, col2 varchar(10), col3 date, col4 float);
INSERT INTO table01 VALUES (1, 'asdfk9', '2020-01-01', 1/2);

-- 作成したテーブルの確認
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