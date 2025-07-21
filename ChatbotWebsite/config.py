import os

class Config:
    DEBUG = False
    SECRET_KEY = os.urandom(32)

    # MySQL database URL (for Docker to access MySQL on host)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        "mysql+pymysql://root:Murali%40123@host.docker.internal/chatbot"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email configuration (keep using env vars for security)
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
