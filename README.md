# mysql-test

## dockerでmysql環境を作成
```shell
docker pull mysql

docker run --name mysql -e MYSQL_ROOT_PASSWORD=mysql -d -p 3306:3306 mysql

# CONTAINER ID を取得
docker ps

# Containerに接続
docker exec -it <CONTAINER ID> bash
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
```