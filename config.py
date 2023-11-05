import os

from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")