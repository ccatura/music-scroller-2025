from flask          import Flask, render_template
from pages.home     import home_bp 
from pages.songs    import songs_bp 
from pages.song     import song_bp 
from pages.user     import user_bp 
from pages.sets     import sets_bp 
from pages.create   import create_bp 
from pages.search   import search_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(songs_bp)
app.register_blueprint(song_bp)
app.register_blueprint(user_bp)
app.register_blueprint(sets_bp)
app.register_blueprint(create_bp)
app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True)

