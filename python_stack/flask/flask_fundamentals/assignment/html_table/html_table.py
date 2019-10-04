# Assignment: HTML Table
# Objectives:
# 1. Get comfortable passing information from the route to the template
# 2. Get very comfortable iterating through a list of dictionaries to generate a html output.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
	users = [
		{'first_name' : 'Michael', 'last_name' : 'Choi'},
		{'first_name' : 'John', 'last_name' : 'Supsupin'},
		{'first_name' : 'Mark', 'last_name' : 'Guillen'},
		{'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
	return render_template('index.html', users = users)

if __name__=="__main__":  
	app.run(debug=True)