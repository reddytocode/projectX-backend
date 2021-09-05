import os
from pathlib import Path

import dotenv

from .settings import *  # noqa

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv.read_dotenv(dotenv=f"{BASE_DIR}/.test.env")

os.environ["DJANGO_DEBUG"] = "true"
os.environ["DJANGO_TESTING"] = "true"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DATABASE_NAME", "projectX"),
        "USER": os.getenv("DATABASE_USER", "root"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", ""),
        "HOST": "127.0.0.1",  # change to localhost if it does not work
        "PORT": os.getenv("DATABASE_PORT", "3306"),
    }
}
