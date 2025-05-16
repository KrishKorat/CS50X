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
  search_query = request.args.get('search', '').strip().lower()
  selected_category = request.args.get('category', '').strip()
  sort_order = request.args.get('sort', '').strip()


  conn = dbConn()

  categories = conn.execute("SELECT DISTINCT category FROM books").fetchall()

  query = "SELECT * FROM books"
  conditions = []
  params = []
  

  if search_query:
    conditions.append("LOWER(title) LIKE ?")
    params.append(f"%{search_query}%")
  

  if selected_category:
    conditions.append("category = ?")
    params.append(selected_category)


  if sort_order == 'asc':
    query += " ORDER BY title ASC"
  elif sort_order == 'desc':
    query += " ORDER BY title DESC"

  
  if conditions:
    query += " WHERE " + " AND ".join(conditions)
  
  books = conn.execute(query, params).fetchall()
  conn.close()

  return render_template(
    'index.html', 
    books=books, 
    search_query=search_query,
    categories = [c[0] for c in categories],
    selected_category=selected_category,
    sort_order=sort_order
  )



@app.route("/add", methods=['GET', 'POST'])
def add_book():

  if request.method == 'POST':
    title = request.form['title']
    author = request.form['author']
    category = request.form['category']

    conn = dbConn()
    conn.execute("INSERT INTO books (title, author, category) VALUES (?, ?, ?)", (title, author, category))
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
    category = request.form['category']

    conn.execute('UPDATE books SET title = ?, author = ?, category = ? WHERE id = ?', (title, author, category, id))

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