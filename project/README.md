
---

# BookShelf – A Personal Book Tracker Web App  
#### Video Demo: <URL HERE>  
#### Description:

MyBookShelf is a simple, lightweight, and functional web-based application that allows users to track their personal reading collection. Built using Python with the Flask micro-framework, SQLite as the database backend, and Bootstrap for responsive design, the application aims to help users store, search, categorize, sort, and manage the books they plan to read, are currently reading, or have completed.

This project was inspired by the need for a minimal and easy-to-use personal library app for book lovers. Instead of relying on complex or feature-heavy commercial tools, MyBookShelf provides a clean, intuitive interface with just the right amount of control and customization.

---

## 📂 Features Overview

- **User Registration and Login**:  
  Users can securely register an account using a username and password. Passwords are hashed using SHA-256 before being stored in the database. A confirm-password field ensures the user doesn’t mistype their credentials. Once logged in, sessions are maintained to keep the user authenticated.

- **Add New Books**:  
  Users can add books to their personal shelf with details including title, author, category, and a reading status (e.g., plan to read, reading, on hold, completed).

- **Edit Book Details**:  
  Each book’s information can be edited, including the reading status, which allows the user to keep track of their progress.

- **Search Functionality**:  
  The app includes a robust search system:
  - **By Book Title**
  - **By Category**
  - **By Sorting (Ascending or Descending Title Order)**  
  All search types are kept logically separate in code for clarity and scalability.

- **Status Filter**:  
  The application allows users to manage their reading journey by assigning a status to each book. This helps keep the bookshelf organized and track progress effectively.

- **Sort Books**:  
  Users can sort books alphabetically by title in ascending or descending order, without needing to click a button — sorting happens as soon as a dropdown option is selected.

- **Responsive UI with Bootstrap**:  
  The UI is styled using Bootstrap 5 to ensure consistency and responsiveness across devices.

---

## 📁 Files and What They Do

- **`app.py`**:  
  This is the main Flask application that handles routing, logic, session handling, database queries, and error management. It includes routes for:
  - `/` (homepage with search/sort/filter functionality)
  - `/add` (add a book)
  - `/edit/<id>` (edit a book)
  - `/delete/<id>` (delete a book)
  - `/register` and `/login` (user auth)
  - `/logout` (session clearing)

- **`templates/index.html`**:  
  The homepage template where books are listed. It includes the search bar, dropdowns for category filter and sort, and links to edit or delete books.

- **`templates/register.html` and `templates/login.html`**:  
  These pages allow users to register and login with simple forms, styled with Bootstrap classes.

- **`templates/edit.html`**:  
  A dynamic form to edit existing book entries, pre-populated with current values.

- **`books.db`**:  
  SQLite3 database file storing all books and user credentials. It has two main tables:
  - `books`: stores id, title, author, category, and status.
  - `users`: stores username and hashed password.

- **`requirements.txt`**:  
  Lists all Python packages required to run the app. Flask and Werkzeug are among the essentials.

---

## ⚙️ Design Decisions

- **Why SQLite?**  
  SQLite was chosen for its simplicity and zero-configuration approach, which makes it perfect for small, local web apps like this one.

- **Why Flask?**  
  Flask’s minimal design allowed full control over routing and app structure, with fewer abstractions than Django.

- **Why SHA-256 for password hashing?**  
  While libraries like bcrypt or Argon2 are recommended for production, SHA-256 was used here for simplicity and educational clarity.

- **UI Simplicity**:  
  Bootstrap was used to rapidly prototype a responsive design without needing custom CSS. The focus was on function, not fancy visuals.

- **Form Handling and Validation**:  
  Minimal JavaScript is used; most features are handled server-side to keep things beginner-friendly. Simple conditional logic handles user feedback, like incorrect passwords or duplicate usernames.

---

## 🚀 How to Run

1. **Install Requirements**  
   ```bash
   pip install -r requirements.txt

2. **Initialize the Database**
   Create a `books.db` file and run the schema creation code once to generate tables.

3. **Run the App**

   ```bash
   flask run
   ```

4. **Access the App**
   Open `http://127.0.0.1:5000` in your browser.

---

## 📌 Future Improvements

* Add book cover image upload
* Allow tagging and multiple categories per book
* Add sort/filter by date added
* Pagination and improved search suggestions
* Allow exporting bookshelf as CSV or JSON

---

## 🏁 Conclusion

MyBookShelf is a fully functional book tracking application ideal for individual users. It was developed with a focus on clarity, modularity, and minimalism. It demonstrates solid foundational knowledge of web development, including authentication, session handling, CRUD operations, dynamic rendering, and secure password storage. It can be extended into a much more powerful system but serves well even in its current lightweight form.

