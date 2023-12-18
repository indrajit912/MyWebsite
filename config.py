"""
Flask App Configuration

This module defines configuration settings for the Flask web application.

"""
import os
from os.path import join, dirname
from dotenv import load_dotenv
from pathlib import Path
from secrets import token_hex

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BASE_DIR = Path(__file__).parent.resolve()
APP_DATA_DIR = Path(__file__).parent / "app_data"

#############################################################################
# Constants required for sending emails using SMTP
INDRAJITS_BOT_EMAIL_ID = os.environ.get("INDRAJITS_BOT_EMAIL_ID")
INDRAJITS_BOT_EMAIL_PASSWD = os.environ.get("INDRAJITS_BOT_APP_PASSWORD")
INDRAJIT912_GMAIL = os.environ.get("INDRAJIT912_GMAIL")
GMAIL_SERVER = ['smtp.gmail.com', 587]
#############################################################################

#############################################################################
# MySQL Database credentials
# Below are the PlanetScale db credentials
DB_HOST = os.environ.get("DB_HOST")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

# Database URI
connection_uri = (
    f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    "?ssl_ca=/etc/ssl/cert.pem"
)
#############################################################################

class Config:
    """
    This is the config class that will be used to create the webapp!
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or token_hex(16)

    SQLALCHEMY_DATABASE_URI = connection_uri \
        or 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = False
