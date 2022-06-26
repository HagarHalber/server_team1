from flask import Blueprint, render_template, request, redirect, url_for, session
import mysql.connector

# home blueprint definition
from utilities.db.db_manager import dbManager

MyProfile = Blueprint('MyProfile', __name__, template_folder='templates', static_folder='static', url_prefix="/MyProfile")


# Routes
@MyProfile.route('/')
def MyProfile_func():
    if session:
        email = session['user_email']
        query_id = "select * from users where email='%s'" % email
        query_result = dbManager.fetch(query_id)
        print(query_result)
        return render_template('myprofile_itamar.html', query_id=query_result)
    return render_template('myprofile_itamar.html')
