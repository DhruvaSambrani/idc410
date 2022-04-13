import sqlite3

CONN = sqlite3.connect("news-recommender.db")
cur = CONN.cursor()
cur.execute('''CREATE TABLE users
           (name text, username text not null primary key, pass text, prefs);''')
cur.execute('''CREATE TABLE articles
           (title text, dop date, summary text, author text, link text);''')
cur.execute('''CREATE TABLE sessions
           (id text, starttime integer, username text, active int);''')
cur.execute('''CREATE TABLE events
           (id text, time integer, event text, value text);''')
cur.close()
CONN.commit()

