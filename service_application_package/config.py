import os
import sys
from datetime import timedelta
from urllib.parse import urlparse

class Config:
	# Ensure default database exists.
	SECRET_KEY = os.environ.get('SECRET_KEY')
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
	PERMANENT_SESSION_LIFETIME = timedelta(days=7)
	CLEARDB_DATABASE_URL = urlparse(os.environ['CLEARDB_DATABASE_URL'])
	MONGO_DBNAME = "items"
	MONGO_URI = os.environ.get('MONGO_URI')