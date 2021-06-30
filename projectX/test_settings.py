import os
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
dotenv.read_dotenv(f"{BASE_DIR}/.env")

os.environ["DJANGO_DEBUG"] = "true"
os.environ["DJANGO_TESTING"] = "true"

# from .settings import *  # noqa: E402
