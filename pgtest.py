import psycopg2

try:
    conn_str = "dbname = 'data_sci' user='postgres' host='localhost' password=***ah***' "
    conn = psycopg2.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute(""" SELECT * FROM staff """)
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Invalid dbname, user or password")
    print(e)
