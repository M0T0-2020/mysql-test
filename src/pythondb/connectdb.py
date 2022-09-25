import os
from sqlalchemy import create_engine

dialect = "mysql"
username = "root"
password = os.environ["MYSQLPASSWORD"]
# hostをlocalhostにするとだめ　(参考):https://qiita.com/hugashy/items/05697f40ae2ccf6a3954
host="127.0.0.1"
port='3306'
database = "python_test"

engine = create_engine(
    f"{dialect}://{username}:{password}@{host}:{port}/{database}?charset=utf8",
    encoding = "utf-8",
    echo=True)
print(engine.connect())