import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="sql647.main-hosting.eu",
        user="u682819236_scroll2",
        password="8h:pPw>m8Nx;",
        database="u682819236_music_scroll2"
    )