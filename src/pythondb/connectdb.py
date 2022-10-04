import datetime
import os
import random
from typing import Any, Dict

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Connection as sqlalchemyCon

dialect = "mysql"
username = "root"
# password = os.environ["MYSQLPASSWORD"]
password = "mysql"
# hostをlocalhostにするとだめ　(参考):https://qiita.com/hugashy/items/05697f40ae2ccf6a3954
host = "127.0.0.1"
port = "3306"
database = "mydb"

engine = create_engine(
    f"{dialect}://{username}:{password}@{host}:{port}/{database}?charset=utf8",
    encoding="utf-8",
    echo=False,
)
print(engine.connect())


def create_table(conn: sqlalchemyCon, n_rows: int = 2000):
    conn.execute(text("""DROP TABLE IF EXISTS table01;"""))
    # col4 にインデックスを貼る
    conn.execute(
        text(
            """
            CREATE table table01
            (
                `id` bigint NOT NULL AUTO_INCREMENT, col1 varchar(128), col2 date, col3 float, col4 int,
                INDEX col4_index (col4),
                PRIMARY KEY (`id`)
            );
            """
        )
    )
    insert_sql: list[str] = []
    insert_value: Dict[str, Any] = {}
    base_date = datetime.datetime.strptime("2022-1-1", "%Y-%m-%d")
    for i in range(n_rows):
        date = base_date + datetime.timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d")
        insert_sql.append(f"(:col1{i}, :col2{i}, :col3{i}, :col4{i})")
        insert_value.update(
            {
                f"col1{i}": f"index{i}",
                f"col2{i}": date_str,
                f"col3{i}": i**1 / 3,
                f"col4{i}": random.randint(0, 16),
            }
        )
    insert_sql = ",".join(insert_sql)
    print(insert_value)
    conn.execute(
        text(
            f"""
            INSERT INTO `table01` (col1, col2, col3, col4)
            VALUES {insert_sql};
            """
        ),
        insert_value,
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


def _get_groupby_col4(conn: sqlalchemyCon, limit: int):
    assert type(limit) == int, "limit must be integer!!"
    result = conn.execute(
        text(
            f"""
            SELECT col4 as `col4`, COUNT(col4) as `count_index`, AVG(col3) as `avg_col3`
            FROM table01
            GROUP BY `col4`
            ORDER BY `col4`
            LIMIT {limit}
            ;
            """
        )
    )
    rows = result.all()
    print(len(rows))
    print(list(result.keys()))
    for i, row in enumerate(rows):
        print(i, row[f"col4"], row[f"count_index"], row["avg_col3"])


def _get_groupby_transform_col4(conn: sqlalchemyCon, limit: int):
    assert type(limit) == int, "limit must be integer!!"

    # explainを使って、Indexが効くか確認
    explain_result = conn.execute(
        text(
            f"""
            EXPLAIN
            SELECT table01.col4, table02.count_index AS `count_col4`, table02.avg_col3 AS `avg_col3`
            FROM 
                table01
                LEFT JOIN (
                    SELECT col4 AS `col4`, COUNT(col4) as `count_index`, AVG(col3)/100 as `avg_col3`
                    FROM table01
                    GROUP BY col4
                ) 
            AS table02
            ON table01.col4 =  table02.col4
            LIMIT {limit}
            ;
            """
        )
    )
    print("EXPLAIN")
    for row in explain_result.all():
        print(row)

    result = conn.execute(
        text(
            f"""
            SELECT table01.col4, table02.count_index AS `count_col4`, table02.avg_col3 AS `avg_col3`
            FROM 
                table01
                LEFT JOIN (
                    SELECT col4 AS `col4`, COUNT(col4) as `count_index`, AVG(col3)/100 as `avg_col3`
                    FROM table01
                    GROUP BY col4
                ) 
            AS table02
            ON table01.col4 =  table02.col4
            LIMIT {limit}
            ;
            """
        )
    )
    rows = result.all()
    print(len(rows))
    print(list(result.keys()))
    try:
        for i, row in enumerate(rows):
            print(i, row[f"col4"], row[f"count_col4"], row[f"avg_col3"])
    except:
        pass


with engine.begin() as conn:
    create_table(conn=conn)
    _get_groupby_col4(conn=conn, limit=10)
    _get_groupby_transform_col4(conn=conn, limit=30)
