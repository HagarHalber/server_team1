from flask import Blueprint, render_template, request, redirect, url_for, session
from utilities.Classes.Users import User
import mysql.connector

# home blueprint definition
from utilities.db.db_manager import dbManager

MyProfile = Blueprint('MyProfile', __name__, template_folder='templates', static_folder='static', url_prefix="/MyProfile")


# Routes
@MyProfile.route('/')
def MyProfile_func():
    if session:
        email = session['user_email']
        user = User(email, None, None, None, None,
                            None, None, None, None,
                            None, None, None, None, None, None, None, None, None, None)
        query_id = user.search_user()
        print(query_id)
        return render_template('myprofile_itamar.html', query_id=query_id)
    return render_template('myprofile_itamar.html')


@MyProfile.route('/deleteProfile', methods=['GET', 'POST'])
def Delete_func():
    if session:
        email = session['user_email']
        user = User(email, None, None, None, None,
                            None, None, None, None,
                            None, None, None, None, None, None, None, None, None, None)
        query_id = user.search_user()
        print(query_id)
        user.delete_user()
        session['logedin'] = False
        return redirect('/Home')
    return render_template('myprofile_itamar.html')
