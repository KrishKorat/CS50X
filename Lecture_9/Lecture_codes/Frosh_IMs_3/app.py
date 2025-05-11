from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)


db = SQL('sqlite:///froshims.db')


SPORTS = ["Baseball", "Soccer", "F1"]


@app.route("/deregister", methods=["POST"])
def deregister():
  
  id = request.form.get("id")
  if id:
    db.execute("DELETE FROM users WHERE id = ?", id)

  return redirect("/registrants")

@app.route("/")
def index():
  return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():

  name = request.form.get("name")
  if not name:
    return render_template("failure.html", msg="Name missing")
  
  sport = request.form.get("sport")
  if not sport:
    return render_template("failure.html", msg="Sport missing")
  
  if sport not in SPORTS:
    return render_template("failure.html", msg="Invalid sport")
  

  db.execute("INSERT INTO users (name, sport) VALUES (?, ?)", name, sport)

  return redirect("/registrants")
  # return render_template("success.html")


@app.route("/registrants")
def registrants():
  registrants = db.execute("SELECT * FROM users")
  return render_template("registrants.html", registrants=registrants)