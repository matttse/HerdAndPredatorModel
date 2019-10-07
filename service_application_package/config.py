import os
import sys
from datetime import timedelta
from urllib.parse import urlparse

class Config:
	# Ensure default database exists.
	PERMANENT_SESSION_LIFETIME = timedelta(days=7)
	SECRET_KEY = os.environ.get('SECRET_KEY')