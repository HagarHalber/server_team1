from flask import Blueprint, render_template
from flask import Flask, redirect
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify


MyMatches = Blueprint('MyMatches', __name__,
                         static_folder='static',
                         template_folder='templates',
                         url_prefix="/MyMatches")

@MyMatches.route('/')
def MyMatches_func():
    return render_template('myMatches.html')