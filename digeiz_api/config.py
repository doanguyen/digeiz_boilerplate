import os
from os.path import join
from pathlib import Path

APP_DIR = Path.cwd()
DB_URI = os.environ.get("DB_URI", default=f"sqlite:////{join(APP_DIR, 'test_api.db')}")
DEBUG = os.environ.get("DEBUG", default=False)
