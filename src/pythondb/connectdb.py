import os
from sqlalchemy import create_engine, text

dialect = "mysql"
username = "root"
password = os.environ["MYSQLPASSWORD"]
# hostをlocalhostにするとだめ　(参考):https://qiita.com/hugashy/items/05697f40ae2ccf6a3954
host="127.0.0.1"
port='3306'
database = "mydb"

engine = create_engine(
    f"{dialect}://{username}:{password}@{host}:{port}/{database}?charset=utf8",
    encoding = "utf-8",
    echo=False)
print(engine.connect())

with engine.begin() as conn:
    result = conn.execute(
        text(
            """
            SELECT * 
            FROM table01;
            """
        )
    )
    rows = result.all()
    for row in rows:
        print(row["col1"], type(row["col1"]))
        print(row["col2"], type(row["col2"]))
        print(row["col3"], type(row["col3"]))
        print(row["col4"], type(row["col4"]))
