from flask import Blueprint, render_template, request, redirect
import mysql.connector

# home blueprint definition
About = Blueprint('About', __name__, template_folder='templates')

# Routes
@About.route('/About')
def About_func():
    return render_template('TripalAboutUs.html')
