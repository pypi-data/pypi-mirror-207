from pms import db_functions
from pms.models import User
import pathlib

db_path = pathlib.Path.joinpath(pathlib.Path(__file__).parent, "sql.db")


def signup_user(username, password):
    with db_functions.CreateConnection(db_path) as connection:
        db_functions.create_db(connection)
        try:
            user = User.signup(connection, username, password)
            print("user add!")
            return user
        except ValueError as v:
            print(v.__str__())


def login_user(username, password):
    with db_functions.CreateConnection(db_path) as connection:
        try:
            User.login(connection, username, password)
            print("user logged in")
        except ValueError as v:
            print(v.__str__())


def get_logged_user(connection):
    user = User.get_logged_user(connection)
    if user is None:
        raise ValueError("login a user first")
    return user


def logout():
    with db_functions.CreateConnection(db_path) as connection:
        if User.logout(connection):
            print("user logged out")
        else:
            print("user not login!")


def display_logged_user():
    with db_functions.CreateConnection(db_path) as connection:
        try:
            user = get_logged_user(connection)
            print(f"logged user is:{user.username}")
        except ValueError:
            print("no user logged")


def delete_user(username, password):
    with db_functions.CreateConnection(db_path) as connection:
        try:
            User.delete(connection, username, password)
            print("user deleted")
        except ValueError as v:
            print(v.__str__())
