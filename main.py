from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    current_date = now.strftime("%d-%m-%y")
    current_time = now.strftime("%H:%M")
    context = {
        "title": "Главная",
        "button": "Продолжить"
    }
    return render_template("index.html", current_date=current_date, current_time=current_time, **context)
    page.refresh(30)

@app.route("/films/")
def films():
    context = {
        "title": "Фильмы",
        "button": "Википедия"
    }
    return render_template("films.html", **context)

@app.route("/about/")
def about():
    context = {
        "title": "О нас",
        "button": "Далее"
    }
    return render_template("about.html",**context)


@app.route("/person/")
def person():
    context = {
        "title": "Герои фильмов",
        "button": "Википедия"
    }
    return render_template("person.html", **context)

@app.route("/blog/")
def blog():
    context = {
        "title": "Блог",
        "button": "Читать статью"
    }
    return render_template("blog.html", **context)

@app.route("/contacts/")
def contacts():
    context = {
        "title": "Контакты",
        "button": "Связаться с нами"
    }
    return render_template("contacts.html", **context)

@app.route("/home/")
def home():
    context = {
        "title": "Домашняя страница",
        "button": "Смотреть фильм"
    }
    return render_template("home.html", **context)

if __name__ == "__main__":
    app.run()