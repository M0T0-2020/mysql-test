import datetime
import os
import random
from typing import Any, Dict
from sqlalchemy.engine import Connection as sqlalchemyCon
from sqlalchemy import create_engine, text

dialect = "mysql"
username = "root"
# password = os.environ["MYSQLPASSWORD"]
password = "mysql"
# hostをlocalhostにするとだめ　(参考):https://qiita.com/hugashy/items/05697f40ae2ccf6a3954
host="127.0.0.1"
port='3306'
database = "mydb"

engine = create_engine(
    f"{dialect}://{username}:{password}@{host}:{port}/{database}?charset=utf8",
    encoding = "utf-8",
    echo=False)
print(engine.connect())


def create_table(conn:sqlalchemyCon):
    conn.execute(text("""DROP TABLE IF EXISTS table01;"""))
    conn.execute(
        text(
            """
            CREATE table table01
            (
                `id` bigint NOT NULL AUTO_INCREMENT, col1 varchar(128), col2 date, col3 float, col4 int,
                PRIMARY KEY (`id`)
            );
            """
        )
    )
    insert_sql:list[str] = []
    insert_value:Dict[str,Any] = {}
    base_date = datetime.datetime.strptime("2022-1-1", "%Y-%m-%d")
    for i in range(2000):
        date = base_date + datetime.timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d")
        insert_sql.append(f"(:col1{i}, :col2{i}, :col3{i}, :col4{i})")
        insert_value.update({
            f"col1{i}": f"index{i}",
            f"col2{i}": date_str,
            f"col3{i}": i**1/3,
            f"col4{i}": random.randint(0,100),
        })
    insert_sql = ",".join(insert_sql)
    print(insert_value)
    conn.execute(
        text(
            f"""
            INSERT INTO `table01` (col1, col2, col3, col4)
            VALUES {insert_sql};
            """),
        insert_value
    )

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

with engine.begin() as conn:
    create_table(conn=conn)