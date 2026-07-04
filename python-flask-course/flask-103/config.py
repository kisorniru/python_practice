import os

class Config:
    SECRET_KEY = "secret_key_here"
    PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(PROJECT_DIR, "database", "sqlite.db")