from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)

app.secret_key = 'greatnumberkey'

@app.route('/')
def index():
    if 'number' in session:
        print(f"Secret number is {session['number']}...")
    else:
        session['number'] = random.randint(1, 100)
        print(f"Secret number is now {session['number']}.")
    # session['guess'] = int(request.form['guess'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    print(f"User guessed {session['guess']}.")
    return redirect('/')

@app.route('/play_again')
def destroy():
    session.clear()
    print('User liked the game so much, they decided to play again!')
    return redirect('/')

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect("show")

# @app.route("/show")
# def show_user():
#     print("Showing the User Info From the Form")
#     print(request.form)
#     return render_template("show.html", name_on_template=session['username'], email_on_template=session['useremail'])

if __name__ == "__main__":
    app.run(debug=True)