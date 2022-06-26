from flask import Blueprint, render_template, request, redirect, session
import mysql.connector

# home blueprint definition
from utilities.Classes.ContactUs_guest import ContactUs_guest

ContectUs = Blueprint('ContectUs', __name__, template_folder='templates')


# Routes
@ContectUs.route('/ContectUs', methods=['GET', 'POST'])
def ContectUs_func():
    if request.method == 'POST':
        name = request.form['Name']
        email = request.form['FromEmailAddress']
        phone = request.form['PhoneNumber']
        contact = request.form['Comments']
        Contact = ContactUs_guest(name, phone, email, contact)
        Contact.add_contact()
    return render_template('TripalContactUs.html')
