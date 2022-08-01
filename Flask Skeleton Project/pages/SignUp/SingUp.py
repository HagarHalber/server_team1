from flask import Blueprint, render_template, request, redirect, url_for, session
from utilities.Classes.Users import User

SignUp = Blueprint('SignUp', __name__,
                   template_folder='templates')


@SignUp.route('/SignUp', methods=['GET', 'POST'])
def SignUp_func():
    if request.method == "POST":
        if 'name' in request.form and 'email' in request.form and 'password' in request.form and 'phone' in request.form:
            session['user_email'] = request.form['email']
            session['user_name'] = request.form['name']
            session['user_password'] = request.form['password']
            session['user_phone'] = request.form['phone']
            session['logedin'] = True
            user = User(session['user_email'], session['user_name'], session['user_password'], session['user_phone'],
                        None, None, None, None, None, None, None,
                        None, None, None, None, None, None, None, None)
            users = user.search_user()
            my_item = next((row for row in users if row[0] == session['user_email']), None)
            if my_item is None:
                user.add_user()
                return redirect(url_for('createProfile.createProfile_func'))
            else:
                return render_template('SignUp.html', message='email already exist please try a new email and sing in')
    return render_template('SignUp.html')


@SignUp.route('/SignIn', methods=['GET', 'POST'])
def SignIn_func():
    if 'email_login' in request.form and 'password_login' in request.form:
        email = request.form['email_login']
        password = request.form['password_login']
        session['logedin'] = True
        user = User(email, None, password, None,
                    None, None, None, None, None, None, None,
                    None, None, None, None, None, None, None, None)
        users = user.search_user()
        if len(users) == 0:
            return render_template('SignUp.html', message='email not exist please try a new email and sing in')
        else:
            if users[0][2] == password:
                session['user_email'] = email
                session['user_password'] = password
                session['user_name'] = users[0][1]
                return redirect('/MyProfile')
            else:
                return render_template('SignUp.html', message='wrong password')
    return render_template('SignUp.html')
