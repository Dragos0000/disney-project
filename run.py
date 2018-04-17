import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "some secret"


@app.route('/')
def index():
	names = []
	posts = []
	with open("data/post.txt", "r") as file:
		lines = file.read().splitlines()

	for i, text in enumerate(lines):
		if i%2 == 0:
			names.append(text)
		else:
			posts.append(text)
	names_and_posts = zip(names, posts)

	
	return render_template("index.html", data= names_and_posts)

@app.route('/',methods=["POST"])
def form_blog():
	
	text = request.form["message"]
	user_name = request.form['name']
	file = open("data/post.txt", "a")
	file.write(user_name + "\n")
	file.write(text + "\n")
	file.close()
	if request.method == "POST":
		flash("Thanks {}, we have received your princess quote! Write one more or revisit Home page to see your post".format(request.form["name"]))
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
	data = []
	with open("data/steps.json", "r") as json_data:
		 data = json.load(json_data)
		 return render_template("careers.html", page_title="Prepare to be a princess", steps_data = data)

if __name__ == '__main__':
    app.run(debug=True)