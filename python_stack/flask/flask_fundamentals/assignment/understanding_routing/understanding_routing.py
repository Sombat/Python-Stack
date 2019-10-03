# Assignment: Understanding Routing
# Objectives:
# 1. Practice building a server with Flask from scratch
# 2. Get comfortable with routes and passing information to the routes

from flask import Flask  # Import Flask to allow us to create our appcopy

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
	return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def success():
	return"Dojo!"

@app.route('/say/<name>')
def hello(name):
	print(name)
	return "Hi " + name + "!"

@app.route('/repeat/<num>/<word>')
def show_user_profile(num, word):
	print(num)
	print(word)
	word = word + " "
	return int(num)*word

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
	app.run(debug=True)    # Run the app in debug mode.