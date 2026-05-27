import os

import psycopg2


def get_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )


def test_can_connect_to_postgres():
    conn = get_connection()

    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM USERS;")
    result = cur.fetchone()

    cur.close()
    conn.close()

    assert result is not None
    assert result[0] >= 0


def test_can_insert_and_read_user():
    conn = get_connection()
    cur = conn.cursor()

    test_name = "jenkins_test_user"
    test_email = "jenkins_test_user@example.com"

    cur.execute(
        """
        INSERT INTO users (first_name, email)
        VALUES (%s, %s)
        RETURNING id;
        """,
        (test_name, test_email),
    )

    row = cur.fetchone()

    assert row is not None

    new_user_id = row[0]

    cur.execute(
        """
        SELECT first_name, email
        FROM users
        WHERE id = %s;
        """,
        (new_user_id,),
    )

    result = cur.fetchone()

    cur.execute(
        """
        DELETE FROM users
        WHERE id = %s;
        """,
        (new_user_id,),
    )

    conn.commit()

    cur.close()
    conn.close()

    assert result is not None
    assert result[0] == test_name
    assert result[1] == test_email
