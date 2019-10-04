# Assignment: Checkerboard
# Objectives:
# 1. Continue to learn how to pass information from the url to the route
# Practice linking static files to templates
# Get comfortable passing information from the route to the template
# Understand how to use for loop properly in the template
# Recognize the value of creating a html/css first and then adding logic/code

from flask import Flask, render_template  # Import Flask and render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
	return render_template('index.html', x=8, y=8, color1='red', color2='black') # Displays board of 8x8

@app.route('/<x>') # Set 8 as defaul amount of rows, and pass in x as the number of columns
def rows(x):
	return render_template('index.html', x=int(x), y=8, color1='red', color2='black')

@app.route('/<x>/<y>')
def columns(x, y):
	return render_template('index.html', x=int(x), y=int(y), color1='red', color2='black') # Pass in x and y as columns and rows

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
	app.run(debug=True)    # Run the app in debug mode.