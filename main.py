from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)


@app.route("/films/")
def films():
    return render_template("films.html")


@app.route("/person/")
def person():
    return render_template("person.html")

@app.route("/blog/")
def blog():
    return render_template("blog.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

@app.route("/")
def home():
    now = datetime.now()
    current_date = now.strftime("%d-%m-%y")
    current_time = now.strftime("%H:%M")

    return render_template("index.html", current_date=current_date, current_time=current_time)
    page.refresh(30)

if __name__ == "__main__":
    app.run()