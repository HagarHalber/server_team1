from flask import Blueprint, render_template, request, redirect, session
import mysql.connector

# home blueprint definition
from utilities.Classes.ContactUs_users import ContactUs_users
from utilities.db.db_manager import dbManager

ContectUsSignin = Blueprint('ContectUsSignin', __name__, template_folder='templates')


# Routes
@ContectUsSignin.route('/ContectUsSignin', methods=['GET', 'POST'])
def ContectUsSignin_func():
    if request.method == 'POST':
        email = session['user_email']
        name = session['user_name']
        contact = request.form['Comments']
        Contact = ContactUs_users(email, contact,name)
        Contact.add_contact()
    return render_template('TripalContactUs_signIn.html')
