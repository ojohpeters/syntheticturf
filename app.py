from flask import Flask, render_template, url_for, redirect, request
from forms import ApplicationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'decb94a1ab5d7b149f12f62b5a7532c3'


@app.route('/')
@app.route('/home')
def Home():
    form = ApplicationForm()
    user_form = request.form
    return render_template("index.html", form=form, user_form=user_form)

@app.route('/apply')
def Apply():
    form = ApplicationForm()
    return render_template("apply.html", form=form)

@app.route('/proccessing')
def Sender_applicationform():
    form = request.form
    Fullname = form.fullname
    Email = form.email
    DOB = form.dob
    Gender = form.gender
    Country = form.country
    


    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
