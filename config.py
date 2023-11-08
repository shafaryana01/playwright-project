import os

from dotenv import load_dotenv

load_dotenv()

LOGIN_PAGE_URL = os.getenv("LOGIN_PAGE_URL")
MAIN_PAGE_URL = os.getenv("MAIN_PAGE_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")