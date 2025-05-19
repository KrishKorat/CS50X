from flask import Flask, render_template, request, redirect, session, flash, url_for
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'Fiwafjwjc3oiu3112193rdfkjkjekja'


def dbConn():
  return sqlite3.connect('books.db')


conn = dbConn()
conn.execute('''
  CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT DEFAULT 'Uncategorized'
  )
''')
conn.close()



@app.route("/")
def index():

  if 'user_id' not in session:
    return redirect(url_for('login'))
  

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





@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username'].strip()
    password = request.form['password']
    confirm = request.form['confirm']

    if password != confirm:
      return "Passwords do not match"
    
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    conn = dbConn()

    try:
      conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password_hash))
      conn.commit()
      conn.close()

      return redirect('/login')
    except:
      return "Username already exist"

  return render_template('register.html')





@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    conn = dbConn()
    user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password_hash)).fetchone()
    conn.close()

    if user:
      session['user_id'] = user[0]
      session['username'] = user[1]
      return redirect('/')
    else:
      return 'Invalid username or password'
    
  return render_template('login.html')





@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect('/login')












if __name__ == '__main__':
  app.run(debug=True)