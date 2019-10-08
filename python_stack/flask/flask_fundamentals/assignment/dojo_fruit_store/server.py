# Assignment: Dojo Fruit Store
# Objectives:
# 1. Practice using git (particularly git clone)
# 2. Get more comfortable with POST and passing information via a form
# 3. Understand how to reference static css or images
# 4. Note the importance of making your key assignments/projects look better
# 5. Understand why rendering HTML on a URL that received a POST is a bad idea

from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    first_name_from_form = request.form['first_name']
    last_name_from_form = request.form['last_name']
    id_from_form = request.form['student_id']
    strawberry_from_form = request.form['strawberry']
    raspberry_from_form = request.form['raspberry']
    apple_from_form = request.form['apple']
    count_of_fruits = int(strawberry_from_form) + int(raspberry_from_form) + int(apple_from_form)
    print(f'Charging {first_name_from_form} {last_name_from_form} for {count_of_fruits} fruits')
    return render_template("checkout.html", first_name_on_template=first_name_from_form, last_name_on_template=last_name_from_form, id_on_template=id_from_form, strawberry_on_template=int(strawberry_from_form), raspberry_on_template=int(raspberry_from_form), apple_on_template=int(apple_from_form), count_of_fruits=count_of_fruits)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    