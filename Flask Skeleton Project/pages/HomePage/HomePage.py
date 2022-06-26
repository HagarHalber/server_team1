from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector

# home blueprint definition
Home = Blueprint('Home', __name__, template_folder='templates')

# Routes
@Home.route('/Home')
def Home_func():
    return render_template('HomePage.html')

@Home.route('/')
def home_func():
    return redirect('/Home')