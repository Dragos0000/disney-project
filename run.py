import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "some secret"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
	data = []
	with open("data/princess.json", "r") as json_data:
		data = json.load(json_data)
	return render_template("about.html", page_title="About", princess_data = data)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact")


@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Prepare to be a princess")

if __name__ == '__main__':
    app.run(debug=True)