from utilities.db.db_manager import dbManager
from flask import Blueprint, render_template
from flask import Flask, redirect
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify
from utilities.Classes.Users import User


MyMatches = Blueprint('MyMatches', __name__,
                         static_folder='static',
                         template_folder='templates',
                         url_prefix="/MyMatches")

@MyMatches.route('/')
def MyMatches_func():
    if session:
        email = session['user_email']
        user = User(email, None, None, None, None,
                    None, None, None, None,
                    None, None, None, None, None, None, None, None, None, None)
        query_result = user.getMatches()
        print(query_result)
        if(len(query_result) == 0):
            return render_template('myMatches.html',
                                   message='There are no matches for you. Try changing your destination or the dates of your trip')
        return render_template('myMatches.html', matches=query_result, length=len(query_result))
    return render_template('myMatches.html', message='There are no matches for you. Try changing your destination or the dates of your trip')


@MyMatches.route('/view_profile/<email>')
def view_profile(email):
    user = User(email, None, None, None, None,
                None, None, None, None,
                None, None, None, None, None, None, None, None, None, None)
    query_result = user.search_user()
    print(query_result)
    return render_template('matchProfile.html', query_id=query_result)

