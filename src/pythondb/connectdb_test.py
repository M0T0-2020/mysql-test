import os
import mysql.connector

password = os.environ["MYSQLPASSWORD"]
# コネクションの作成
conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password=password,
    database='mydb'
)

# コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect=True)

# 接続できているかどうか確認
print(conn.is_connected())