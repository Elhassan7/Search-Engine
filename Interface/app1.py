
from flask import Flask, render_template, request, session, redirect,url_for
from matplotlib.style import use

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    global userSearch
    userSearch= request.form.get("userSearch")
    return render_template("home.html")


@app.route("/result", methods=['GET', 'POST'])
def search():
    return render_template("result.html", userSearch= userSearch)
