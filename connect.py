import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file


def get_connection():
    return mysql.connector.connect(
        host="sql647.main-hosting.eu",
        user="u682819236_scroll2",
        password=os.getenv("DB_PASSWORD"),
        database="u682819236_music_scroll2"
    )


