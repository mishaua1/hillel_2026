import psycopg2
import pytest
import allure

import os

DB_CONFIG = {
    "dbname": "test_db",
    "user": "test_user",
    "password": "test_password",
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5440"),
}


@pytest.fixture
def connection():
    conn = psycopg2.connect(**DB_CONFIG)
    yield conn
    conn.close()


@pytest.fixture
def cursor(connection):
    cur = connection.cursor()
    cur.execute("DROP TABLE IF EXISTS users;")
    cur.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        );
    """)
    connection.commit()
    yield cur
    cur.close()


@allure.feature("Connection")
def test_connection(connection):
    with allure.step("Перевірка що конект живий"):
        assert connection.closed == 0


@allure.feature("Insert")
def test_insert(cursor, connection):
    with allure.step("Додаємо юзера"):
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;",
            ("Alice", "alice@test.com"),
        )
        user_id = cursor.fetchone()[0]
        connection.commit()

    with allure.step("Дивимось чи вернувся id"):
        assert user_id is not None


@allure.feature("Select")
def test_select(cursor, connection):
    with allure.step("Додаємо Bob"):
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s);",
            ("Bob", "bob@test.com"),
        )
        connection.commit()

    with allure.step("Дістаємо його з бази"):
        cursor.execute("SELECT name, email FROM users WHERE name = %s;", ("Bob",))
        row = cursor.fetchone()

    with allure.step("Звіряємо дані"):
        assert row == ("Bob", "bob@test.com")


@allure.feature("Update")
def test_update(cursor, connection):
    with allure.step("Додаємо Carol"):
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s);",
            ("Carol", "carol@test.com"),
        )
        connection.commit()

    with allure.step("Міняємо їй пошту"):
        cursor.execute(
            "UPDATE users SET email = %s WHERE name = %s;",
            ("new_carol@test.com", "Carol"),
        )
        connection.commit()

    with allure.step("Перевіряємо що пошта нова"):
        cursor.execute("SELECT email FROM users WHERE name = %s;", ("Carol",))
        assert cursor.fetchone()[0] == "new_carol@test.com"


@allure.feature("Delete")
def test_delete(cursor, connection):
    with allure.step("Додаємо Dave"):
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s);",
            ("Dave", "dave@test.com"),
        )
        connection.commit()

    with allure.step("Видаляємо його"):
        cursor.execute("DELETE FROM users WHERE name = %s;", ("Dave",))
        connection.commit()

    with allure.step("Перевіряємо що його вже нема"):
        cursor.execute("SELECT * FROM users WHERE name = %s;", ("Dave",))
        assert cursor.fetchone() is None