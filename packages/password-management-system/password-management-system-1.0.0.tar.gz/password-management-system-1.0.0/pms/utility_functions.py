import random
import re
import string

import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

UPPER_CASE = string.ascii_uppercase
LOWER_CASE = string.ascii_lowercase
NUMBERS = string.digits
SPECIAL_CHAR = "!@#$%*,._"
#      & - have special meaning in cli, so they aren't included in the query


def generate_password(length=16, char_query=None):
    if char_query is None:
        char_query = [UPPER_CASE, LOWER_CASE, NUMBERS, SPECIAL_CHAR]

    if len(char_query) > length:
        raise ValueError("char query can't be longer than the password!")
    my_password=[]
    # use at least 1 char from every query
    for item in char_query:
        index = random.randint(0, len(my_password))
        my_password[index:index] = random.choice(item)
    char_range = "".join(char_query)  # a string of all queries combined to generate the rest of the password
    while len(my_password)<length:
        index = random.randint(0, len(my_password))
        my_password[index:index] = random.choice(char_range)

    print("".join(my_password))


def evaluate_password(password):
    strength = 5
    tips_list=[]
    if len(password)<4:
        print("password strength is 0 from 5")
        print("password is too short to even consider as password!")
    elif len(password)<8:
        tips_list.append("password is short, add more symbols to it")
        strength -= 1

    if re.search(r"\d", password) is None:
        tips_list.append("add numbers")
        strength -= 1

    if re.search(r"[A-Z]", password) is None:
        tips_list.append("add uppercase letters")
        strength -= 1

    if re.search(r"[a-z]", password) is None:
        tips_list.append("add lowercase letters")
        strength -= 1

    if re.search('['+SPECIAL_CHAR+"&-"+']', password) is None:
        tips_list.append("add special characters")
        strength -= 1

    result = (strength, "\n".join(tips_list))
    print(f"password strength is {result[0]} from 5")
    if result[1]:
        print(f"tips to make your password stronger:\n{result[1]}")


def encrypt(password, salt, data):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    return f.encrypt(data)


def decrypt(password, salt, data):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    return f.decrypt(data)


def sha512_hash(password):
    return hashlib.sha512(password.encode('utf-8')).hexdigest()

