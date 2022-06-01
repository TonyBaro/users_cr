from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__)
app.secret_key = 'this_is_getting_way_too_confusing'

@app.route('/')
def index():
    users = User.retrieve()
    return render_template('index.html', all_users = users)

@app.route('/users/new')
def new():
    return render_template('newuser.html')

@app.route('/add_user' , methods=["POST"])
def add():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.add_user(data)
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)