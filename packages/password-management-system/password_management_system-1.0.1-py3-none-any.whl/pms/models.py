import os
from cryptography.fernet import Fernet

from pms.utility_functions import encrypt, decrypt, sha512_hash
from pms import db_functions

PASSWORD_PREFIX = """
YrdL6Uw@ZnN,R%AWzEuc!eCjAQ30,_UWzGD@N.JiH9,$7fiXfHcE5vanpuWNVENlur6%Od8PhC%yYSlaJ$tVQU63Cckk521QX9jysSB!bqK3UA3V5qsVt$Z5
PQZU6js*fx2TUoao%$ZY0ZPKh8r6z@6%FhPTePLDmlOYL!kpUtkwMoWFn5oP7N!z7ZGCh%m!i4nItNsa@IdtNwD,v7eQJy1dkbb0E!o*VbezM!4JvqOOHe.o
0@gPbpn9BmeiGHjZz$S#UPsWNvHq%83PYl6yvG2tJv3Cz4.!G8Ohzpdk,kz."""


class User:
    def __init__(self, username):
        self.username = username
        self.hashed_password = ""
        self.key = None
        self.salt=""

    @staticmethod
    def signup(connection, username, password):
        password = User.password_processing(username, password)
        if User.select_user_from_db(connection, username):
            raise ValueError("username already in db")
        password = password
        user = User(username)
        user.key = Fernet.generate_key()
        user.salt = os.urandom(16)
        encrypted_key = encrypt(str.encode(password), user.salt, user.key)
        encrypted_key = int.from_bytes(encrypted_key, byteorder='big')
        user.salt = int.from_bytes(user.salt, byteorder='big')
        user.hashed_password = sha512_hash(password)
        add_user = f"""
            INSERT INTO user (username, password, secret_key, salt)
             VALUES ("{username}", "{user.hashed_password}", "{encrypted_key}", "{user.salt}")
            """
        db_functions.execute_query(connection, add_user)
        return user

    @staticmethod
    def login(connection, username, password):
        if User.get_logged_user(connection) is not None:
            raise ValueError("a user is already logged in")
        password = User.password_processing(username, password)
        user_data = User.select_user_from_db(connection, username)
        if not user_data:
            raise ValueError("username or password incorrect")
        user_data = user_data[0]
        password = password
        hashed_password = sha512_hash(password)
        if hashed_password != user_data[1]:
            raise ValueError("username or password incorrect")
        user = User(username)
        user.hashed_password = hashed_password
        salt = int(user_data[3])
        salt= salt.to_bytes(length=16, byteorder='big')
        encrypted_key = int(user_data[2])
        encrypted_key = encrypted_key.to_bytes(length=140, byteorder='big')
        user.key = decrypt(str.encode(password), salt, encrypted_key)
        db_functions.execute_query(connection, f"""
                    INSERT INTO loggedIn (username, key)
                     VALUES ("{user.username}", "{user.key.decode()}")
                    """)
        return user

    @staticmethod
    def select_user_from_db(connection, username):
        user_data = db_functions.execute_read_query(connection, f"""
                    SELECT * FROM user WHERE username="{username}";
                    """)
        return user_data

    @staticmethod
    def password_processing(username, password):
        return PASSWORD_PREFIX+password+username

    @staticmethod
    def get_logged_user(connection):
        user_data= db_functions.execute_read_query(connection, "SELECT * FROM loggedIn")
        if not user_data:
            return None
        user_data = user_data[0]
        user = User(user_data[0])
        user.key = user_data[1].encode()
        return user

    @staticmethod
    def logout(connection):
        if User.get_logged_user(connection) is not None:
            db_functions.execute_query(connection, "DELETE FROM loggedIn")
            return True
        return False

    @staticmethod
    def delete(connection, username, password):
        password = User.password_processing(username, password)
        user_data = User.select_user_from_db(connection, username)
        if not user_data:
            raise ValueError("username or password incorrect")
        user_data = user_data[0]
        password = password
        hashed_password = sha512_hash(password)
        if hashed_password != user_data[1]:
            raise ValueError("username or password incorrect")
        db_functions.execute_query(connection, f"DELETE FROM password WHERE username = \"{username}\"")
        db_functions.execute_query(connection, f"DELETE FROM loggedIn WHERE username = \"{username}\"")
        db_functions.execute_query(connection, f"DELETE FROM user WHERE username = \"{username}\"")


class Password:
    def __init__(self):
        self.id = None
        self.username = None
        self.password = None
        self.name = None
        self.website = None
        self.description = None

    @staticmethod
    def add_password(connection, user, password, name, website="", description=""):
        if user.key is None:
            raise ValueError("user isn't login")
        if website is None:
            website = ""
        if description is None:
            description = ""
        f = Fernet(user.key)
        password = f.encrypt(password.encode()).decode()
        add_password = f"""
                    INSERT INTO password (username, password, password_name, website, description)
                     VALUES ("{user.username}", "{password}", "{name}", "{website}", "{description}")
                    """
        db_functions.execute_query(connection, add_password)

    @staticmethod
    def db_data_to_list(password_data, key):
        password_list = []
        for item in password_data:
            password = Password()
            password.id = item[0]
            password.username = item[1]
            f = Fernet(key)
            password.password = f.decrypt(item[2].encode()).decode()
            password.name = item[3]
            password.website = item[4]
            password.description = item[5]
            password_list.append(password)
        return password_list

    @staticmethod
    def select_password(connection, user, name=None, website=None, password_id=None):
        if user.key is None:
            raise ValueError("user isn't login")
        condition =""
        if name is not None:
            condition = f' AND password_name="{name}"'
        elif website is not None:
            condition = f' AND website="{website}"'
        elif password_id is not None:
            condition = f' AND id="{password_id}"'
        password_data = db_functions.execute_read_query(connection, f"""
                                SELECT * FROM password WHERE username="{user.username}"{condition};
                                """)
        if not password_data:
            return None
        return Password.db_data_to_list(password_data, user.key)

    @staticmethod
    def delete_password(connection, user, password_id):
        password = Password.select_password(connection, user, password_id=password_id)
        if password is None:
            raise ValueError("delete failed: password not found")
        db_functions.execute_query(connection, f"DELETE FROM password WHERE id = \"{password_id}\"")

    def __str__(self):
        my_str = f"id:{self.id} "
        my_str += f"password:\"{self.password}\" "
        my_str += f"name:{self.name} "
        my_str += f"website:{self.website} "
        my_str += f"description:{self.description}"
        return my_str

    @staticmethod
    def update_password(connection, user, password_id, new_password=None, new_name=None, new_website=None,
                        new_description=None):
        password = Password.select_password(connection, user, password_id=password_id)
        if password is None:
            raise ValueError("password id is invalid")
        field_list=[]
        if new_password is not None:
            f = Fernet(user.key)
            new_password = f.encrypt(new_password.encode()).decode()
            field_list.append(f"password=\"{new_password}\"")
        if new_name is not None:
            field_list.append(f"password_name=\"{new_name}\"")
        if new_website is not None:
            field_list.append(f"website=\"{new_website}\"")
        if new_description is not None:
            field_list.append(f"description=\"{new_description}\"")
        if not field_list:
            raise ValueError("you need to update at least 1 field")
        query = f"""
        UPDATE password SET
        {",".join(field_list)}
        WHERE id = \"{password_id}\"        
        """
        db_functions.execute_query(connection, query)
