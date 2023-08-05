import sqlite3
from sqlite3 import Error


def delete_db(path):
    import os
    os.remove(path)


class CreateConnection:
    def __init__(self, path):
        self.connection = None
        self.path = path

    def __enter__(self):
        connection = None
        try:
            connection = sqlite3.connect(self.path)
        except Error as e:
            print(f"The error '{e}' occurred")
        self.connection = connection
        return connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred (signup to create the database)")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred (signup to create the database)")


def create_db(connection):

    create_user_table="""
    CREATE TABLE IF NOT EXISTS user (
      username TEXT PRIMARY KEY,
      password TEXT NOT NULL,
      secret_key TEXT NOT NULL,
      salt TEXT,
      email TEXT
    );
    """
    execute_query(connection, create_user_table)

    create_password_table="""
    CREATE TABLE IF NOT EXISTS password (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT NOT NULL,
      password TEXT NOT NULL,
      password_name TEXT NOT NULL,
      website TEXT,
      description TEXT,
      FOREIGN KEY(username) REFERENCES user(username)
    );
    """
    execute_query(connection, create_password_table)

    create_logged_in_table = """
    CREATE TABLE IF NOT EXISTS loggedIn (
      username PRIMARY KEY,
      key TEXT,
      FOREIGN KEY(username) REFERENCES user(username)
    );
    """
    execute_query(connection, create_logged_in_table)
