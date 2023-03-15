import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect(
    dbname='taxidb',
    user='postgres',
    password='developer006',
    host='localhost',
    port=5432
)


def add_data():
    a = int(input("id:"))
    b = input("name:")
    cur = connection.cursor(cursor_factory=RealDictCursor)

    sql = "insert into test(id, name) values (%s, %s)"
    value = (a, b)
    cur.execute(sql, value)
    connection.commit()
    cur.close()


add_data()

# cur.execute("select * from staffs where id=%s", (4,))
# cars = cur.fetchall()
# cars2 = cur.fetchone()
# cars2 = cur.fetchmany(2)

# with connection.cursor(cursor_factory=RealDictCursor) as cur:
#     cur.execute("select * from staffs where id=%s", (4,))
#     staffs = cur.fetchall()
#     print("with context manager", cars)
