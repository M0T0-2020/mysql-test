# mysql-test

## dockerでmysql環境を作成
```shell
docker pull mysql

docker run --name mysql -e MYSQL_ROOT_PASSWORD=mysql -d -p 3306:3306 mysql

# CONTAINER ID を取得
docker ps

# CONTAINER IDとパスワードを保存
export CONTAINERID=<CONTAINER ID>
export MYSQLPASSWORD=mysql

# Containerに接続
docker exec -it $CONTAINERID bash
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

## python3.7環境の作成
```shell
python3.7 -m venv venv37
source venv37/bin/activate
pip install -U pip
pip install -r requirements.txt
```