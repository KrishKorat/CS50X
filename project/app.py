from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def dbConn():
  return sqlite3.connect('books.db')


conn = dbConn()
conn.execute('''
  CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL 
  )
''')
conn.close()



@app.route("/")
def index():
  conn = dbConn()
  books = conn.execute("SELECT * FROM books").fetchall()
  conn.close()
  return render_template('index.html', books=books)



@app.route("/add", methods=['GET', 'POST'])
def add_book():

  if request.method == 'POST':
    title = request.form['title']
    author = request.form['author']

    conn = dbConn()
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()

    return redirect('/')
  
  return render_template('add_book.html')



@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_book(id):
  conn = dbConn()

  if request.method == 'POST':
    title = request.form['title']
    author = request.form['author']

    conn.execute('UPDATE books SET title = ?, author = ? WHERE id = ?', (title, author, id))

    conn.commit()
    conn.close()

    return redirect('/')
  
  book = conn.execute("SELECT * FROM books WHERE id = ?", (id,)).fetchone()
  conn.close()

  return render_template('edit_book.html', book=book)



@app.route('/delete/<id>')
def delete_book(id):
  conn = dbConn()
  conn.execute('DELETE FROM books WHERE id = ?', (id,))
  conn.commit()
  conn.close()

  return redirect('/')




if __name__ == '__main__':
  app.run(debug=True)