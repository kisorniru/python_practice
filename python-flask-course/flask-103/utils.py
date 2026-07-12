import hashlib
import os


def hash_password(password):
    salt = os.urandom(16).hex()
    salted_password = password + salt
    hashed = hashlib.sha256(salted_password.encode()).hexdigest()
    return f"{salt}:{hashed}"


def verify_password(db_password, input_password):
    salt, stored_hash = db_password.split(':')
    salted_password = input_password + salt
    hashed = hashlib.sha256(salted_password.encode()).hexdigest()
    return stored_hash == hashed

