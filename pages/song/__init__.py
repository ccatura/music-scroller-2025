from flask import Blueprint, render_template
from connect import get_connection  # import the function, not the old conn

# Define the blueprint
song_bp = Blueprint('song', __name__, template_folder='templates')

@song_bp.route('/song/<int:song_id>')
def show_song(song_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM songs WHERE id = %s", (song_id,))
    song = cursor.fetchone()
    cursor.close()
    conn.close()

    if song:
        return render_template('song.html', song=song, title=song['title'])
    else:
        return "Song not found", 404