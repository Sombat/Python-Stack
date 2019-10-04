# Assignment: Dojo Survey
# Objectives:
# 1. Practice creating a server with Flask from scratch
# 2. Practice adding routes to a Flask app
# 3. Practice having the client send data to the server with a form
# 4. Practice having the server render a template using data provided by the client

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    return render_template("show.html", name_on_template=name_from_form, location_on_template=location_from_form, language_on_template=language_from_form, comment_on_template=comment_from_form)

if __name__ == "__main__":
    app.run(debug=True)