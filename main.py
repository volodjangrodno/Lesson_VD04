from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def films():
    return render_template("index.html")


@app.route("/person/")
def person():
    return render_template("LessonVD04.html")

@app.route("/home/")
def home():
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    return render_template("home.html", current_date=current_date, current_time=current_time)


if __name__ == "__main__":
    app.run()