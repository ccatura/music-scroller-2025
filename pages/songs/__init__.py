from flask import Blueprint, render_template
from connect import get_connection  # use the new connection function

# Create the blueprint
songs_bp = Blueprint('songs', __name__, template_folder='templates')

def get_songs():
    conn = get_connection()  # get a fresh connection
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT `title`, `sub_title`, `id`
        FROM songs
        WHERE user_name LIKE 'arnold'
        ORDER BY title ASC
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

@songs_bp.route('/songs')
def songs():
    songs = get_songs()
    song_quantity = len(songs)
    return render_template('songs.html', title="Songs", data=songs, song_quantity=song_quantity)
