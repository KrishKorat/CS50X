import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response





@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    rows = db.execute("""
        SELECT symbol, SUM(shares) as total_shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING total_shares > 0
    """, user_id)

    holdings = []
    total_value = 0


    for row in rows:

        symbol = row["symbol"]
        shares = row["total_shares"]
        stock = lookup(symbol)

        if stock:
            price = stock["price"]
            total = price * shares
            total_value += total

            holdings.append({
                "symbol": symbol,
                "name": stock["name"],
                "shares": shares,
                "price": price,
                "total": total
            })
    
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    grand_total = total_value + cash

    return render_template("index.html", holdings=holdings, cash=cash, grand_total=grand_total)





@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate symbol
        if not symbol:
            return apology("must provide symbol")
        stock = lookup(symbol)
        if not stock:
            return apology("invalid stock symbol")

        # Validate shares
        if not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("shares must be a positive integer")
        shares = int(shares)


        user_id = session["user_id"]
        rows = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = rows[0]["cash"]

        price = stock["price"]
        total_cost = price * shares


        if total_cost > cash:
            return apology("can't afford")
        
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", user_id, stock["symbol"], shares, price)
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)

        return redirect("/")
    
    else:
        return render_template("buy.html")





@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")






@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("must provide stock symbol")

        stock = lookup(symbol)

        if stock is None:
            return apology("invalid symbol")
        
        return render_template("quoted.html", stock=stock)
    
    else:
        return render_template("quote.html")





@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Username
        username = request.form.get("username")
        if not username:
            return apology("must provide username")

        # Password
        password = request.form.get("password")
        if not password:
            return apology("must provide password")

        # Conformation
        conformation = request.form.get("conformation")
        if not conformation:
            return apology("must provide conformation password")
        
        if password != conformation:
            return apology("must provide same password")
        

        hash_pw = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_pw)
        except:
            return apology("username already exists")
        

        user_id = db.execute("SELECT id FROM users WHERE username = ?", username)[0]["id"]
        session["user_id"] = user_id

        return redirect("/")
    
    else:
        return render_template("register.html")






@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares_input = request.form.get("shares")

        if not symbol:
            return apology("must select a stock")

        if not shares_input or not shares_input.isdigit() or int(shares_input) <= 0:
            return apology("shares must be a positive integer")
        shares_to_sell = int(shares_input)

        row = db.execute("""
            SELECT SUM(shares) as total_shares FROM transactions
            WHERE user_id = ? AND symbol = ?
            GROUP BY symbol
        """, user_id, symbol)

        if not row or row[0]["total_shares"] < shares_to_sell:
            return apology("not enough shares")

        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol")

        price = stock["price"]
        total_earnings = price * shares_to_sell

        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   user_id, symbol, -shares_to_sell, price)

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_earnings, user_id)

        return redirect("/")

    else:
        rows = db.execute("""
            SELECT symbol FROM transactions
            WHERE user_id = ?
            GROUP BY symbol
            HAVING SUM(shares) > 0
        """, user_id)

        symbols = [row["symbol"] for row in rows]
        return render_template("sell.html", symbols=symbols)
