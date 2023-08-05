from pms import db_functions
from pms.user_controller import db_path, get_logged_user
from pms.models import Password


def add_password(new_password, name, website="", description=""):
    with db_functions.CreateConnection(db_path) as connection:
        try:
            user = get_logged_user(connection)
            Password.add_password(connection, user, new_password, name, website, description)
            print("password add!")
        except ValueError as v:
            print(v.__str__())


def select_password(name=None, password_website=None, password_id=None):
    with db_functions.CreateConnection(db_path) as connection:
        try:
            user = get_logged_user(connection)
            password_list = Password.select_password(connection, user, name, password_website, password_id)
            if password_list is None:
                print("no passwords matching found!")
            else:
                for item in password_list:
                    print(item)
        except ValueError as v:
            print(v.__str__())


def delete_password(password_id):
    with db_functions.CreateConnection(db_path) as connection:
        try:
            user = get_logged_user(connection)
            Password.delete_password(connection, user, password_id)
            print("password deleted")
        except ValueError as v:
            print(v.__str__())


def update_password(password_id, new_password=None, new_name=None, new_website=None, new_description=None):
    with db_functions.CreateConnection(db_path) as connection:
        try:
            user = get_logged_user(connection)
            Password.update_password(connection, user, password_id, new_password, new_name, new_website, new_description)
            print("password updated")
        except ValueError as v:
            print(v.__str__())