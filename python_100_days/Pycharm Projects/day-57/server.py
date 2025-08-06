import random
import requests
from datetime import datetime
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, curr_year=current_year)

@app.route("/guess/<name>")
def guess_name(name):
    parameters = {
        "name": name
    }
    response = requests.get("https://api.genderize.io", params=parameters)
    gender = response.json()["gender"]

    response = requests.get("https://api.agify.io", params=parameters)
    age = response.json()["age"]

    return render_template("gender_age.html", name=name, gender=gender, age=age)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)