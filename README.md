# mysql-test

## dockerでmysql環境を作成
```shell
docker pull mysql

docker run --name mysql -e MYSQL_ROOT_PASSWORD=mysql -d -p 3306:3306 mysql

# これでContainer IDを取得
docker ps

# Containerに接続
docker exec -it 'CONTAINER ID' bash
```
## mysqlにログイン　パスワードは mysql
```bash
mysql -u root -p
```