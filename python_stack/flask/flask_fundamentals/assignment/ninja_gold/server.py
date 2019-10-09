from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)

app.secret_key = 'ninjagoldkey'

@app.route('/')
def index():
    if 'gold' in session:
        print(f"Ninja has {session['gold']}.")
    else:
        session['gold'] = 0
        print(f"Ninja just walked in the door.")
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    if request.form['building'] == 'farm':
        if random.randint(1, 2) < 2:
            session['gold'] = session['gold'] - random.randint(10, 20)
        else:
            session['gold'] = session['gold'] + random.randint(10, 20)
    elif request.form['building'] == 'cave':
        if random.randint(1, 2) < 2:
            session['gold'] = session['gold'] - random.randint(5, 10)
        else:
            session['gold'] = session['gold'] + random.randint(5, 10)
    elif request.form['building'] == 'house':
        if random.randint(1, 2) < 2:
            session['gold'] = session['gold'] - random.randint(2, 5)
        else:
            session['gold'] = session['gold'] + random.randint(2, 5)
    elif request.form['building'] == 'casino':
        temp = random.randint(0, 50)
        if random.randint(1, 2) < 2:
            session['gold'] = session['gold'] - temp
            print(f"Entered a casino and lost {temp} golds... Ouch.")
        else:
            session['gold'] = session['gold'] + temp
            print(f"Earned {temp} golds from casino!")

    session['guess'] = int(request.form['guess'])
    print(f"User guessed {session['guess']}.")
    return redirect('/')

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