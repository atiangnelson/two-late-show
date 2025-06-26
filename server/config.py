import os

DATABASE_URI = "postgresql://student:12345@localhost:5432/late_show_db"
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = SECRET_KEY
