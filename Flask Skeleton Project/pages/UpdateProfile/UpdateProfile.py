from flask import Blueprint, render_template, request, redirect, url_for, session
from utilities.Classes.Users import User

updateProfile = Blueprint('updateProfile', __name__,
                          static_folder='static',
                          template_folder='templates',
                          url_prefix="/updateProfile")


@updateProfile.route('/', methods=['GET', 'POST'])
def updateProfile_func():
    if request.method == 'POST':
        if 'first_Name' in request.form and 'last_Name' in request.form:
            email = session['user_email']
            first_name = request.form['first_Name']
            last_name = request.form['last_Name']
            Age = request.form['Age']
            first_time = request.form['first_time']
            destination = request.form['destination']
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            language = request.form['language']
            budget = request.form['budget']
            hobbies = request.form['hobbies']
            vibe = request.form['vibe']
            url = request.form['filename']
            about = request.form['about_me']
            facebook = request.form['facebook']
            instagram = request.form['instagram']
            if first_time == 'on':
                first_time_res = 'true'
            else:
                first_time_res = 'false'
            user = User(email, None, None, None, first_name,
                        last_name, Age, first_time, destination,
                        start_date, end_date, language, budget, hobbies, vibe, url, about, facebook, instagram)
            user.update_user()
            print(email)
            print(url)
            return redirect('/MyProfile')
    return render_template('UpdateProfile.html')
