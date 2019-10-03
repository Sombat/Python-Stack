# Assignment: Playground
# Objectives:
# 1. Get comfortable passing information from the route to the template
# 2. Understand how to display information passed from the route in the template file
# 3. Get comfortable using for loops in the template file
# 4. Get comfortable using if statements in the template file

from flask import Flask, render_template  # Import Flask and render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
	return render_template('index.html', repeat=0, color='blue') # Displays index.html using render_template

@app.route('/play')
def play():
	return render_template('index.html', repeat=3, color='blue') # Displays index.html, passing 3 and blue and defaults

@app.route('/play/<repeat>')
def repeat(repeat):
	return render_template('index.html', repeat=int(repeat), color='blue')  # Displays index.html, passing repeat as an int and blue as the default color

@app.route('/play/<repeat>/<color>')
def color(repeat, color):
	return render_template('index.html', repeat=int(repeat), color=color) # Displays index.html, passing repeat as an int and color

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
	app.run(debug=True)    # Run the app in debug mode.