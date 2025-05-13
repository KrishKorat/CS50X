from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'books.db'

# ----- Utility Functions -----
def connect_db():
    return sqlite3.connect(DATABASE)

def init_db():
    with connect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL
            )
        ''')

# Initialize DB on startup
init_db()

# ----- Routes -----

@app.route('/')
def index():
    conn = connect_db()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        conn = connect_db()
        conn.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    conn = connect_db()
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        conn.execute('UPDATE books SET title = ?, author = ? WHERE id = ?', (title, author, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    book = conn.execute('SELECT * FROM books WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('edit_book.html', book=book)

@app.route('/delete/<int:id>')
def delete_book(id):
    conn = connect_db()
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
