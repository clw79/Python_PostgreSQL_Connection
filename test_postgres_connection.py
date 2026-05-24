import os

import psycopg2


def test_can_connect_to_postgres():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM USERS;")
    result = cur.fetchone()

    cur.close()
    conn.close()

    assert result is not None
    assert result[0] >= 0
