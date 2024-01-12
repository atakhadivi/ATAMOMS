from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired
import requests
from bs4 import BeautifulSoup
import re
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Connect to the SQLite database or create it if it doesn't exist
conn = sqlite3.connect('videos.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS videos
             (title TEXT, url TEXT, embed TEXT, categories TEXT)''')


class VideoForm(FlaskForm):
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = VideoForm()
    rss_url = 'https://www.porn.com/rss'  # Replace with the actual RSS feed URL
    response = requests.get(rss_url)
    soup = BeautifulSoup(response.content, 'xml')
    videos = []

    for item in soup.find_all('item'):
        title = item.title.text
        link = item.link.text
        if 'mom' not in title.lower():
            videos.append((title, link))

    if form.validate_on_submit():
        title, link = form.title.data, form.url.data
        c.execute("INSERT INTO videos VALUES (?, ?, '', ?)", (title, link, ''))
        conn.commit()
        flash('Video added successfully.', 'success')
        return redirect(url_for('index'))

    return render_template('index.html', form=form, videos=videos)


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if not query:
        return redirect(url_for('index'))

    c.execute("SELECT * FROM videos WHERE title LIKE ? OR url LIKE ?",
              ('%' + query + '%', '%' + query + '%'))
    results = c.fetchall()

    return render_template('search.html', query=query, results=results)


@app.route('/video/<string:title>', methods=['GET'])
def video(title):
    c.execute("SELECT * FROM videos WHERE title=?", (title,))
    video = c.fetchone()

    if not video:
        return redirect(url_for('index'))

    embed_url = f'https://www.porn.com/embed/{video[2]}' if video[2] else None
    return render_template('video.html', title=title, url=video[1], embed=embed_url)


@app.route('/like/<string:title>', methods=['GET'])
def like(title):
    c.execute(
        "UPDATE videos SET categories=categories || 'like' WHERE title=?", (title,))
    conn.commit()
    return redirect(url_for('video', title=title))


@app.route('/dislike/<string:title>', methods=['GET'])
def dislike(title):
    c.execute(
        "UPDATE videos SET categories=categories || 'dislike' WHERE title=?", (title,))
    conn.commit()
    return redirect(url_for('video', title=title))


@app.route('/report/<string:title>', methods=['GET'])
def report(title):
    c.execute("DELETE FROM videos WHERE title=?", (title,))
    conn.commit()
    return redirect(url_for('index'))


@app.route('/categories', methods=['GET'])
def categories():
    c.execute("SELECT DISTINCT categories FROM videos")
    categories = c.fetchall()
    return render_template('categories.html', categories=categories)


@app.route('/category/<string:category>', methods=['GET'])
def category(category):
    c.execute("SELECT * FROM videos WHERE categories LIKE ?",
              ('%' + category + '%',))
    results = c.fetchall()
    return render_template('category.html', category=category, results=results)


if __name__ == '__main__':
    app.run(debug=True)
