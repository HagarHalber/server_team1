import os

from flask import Blueprint, render_template, request, redirect, url_for, session, current_app, app
from utilities.Classes.Users import User
from utilities.db.db_manager import dbManager
from werkzeug.utils import secure_filename

createProfile = Blueprint('createProfile', __name__,
                          static_folder='static',
                          template_folder='templates',
                          url_prefix="/createProfile")


@createProfile.route('/', methods=['GET', 'POST'])
def createProfile_func():
    if request.method == 'POST':
        session['logedin'] = True
        if 'first_Name' in request.form and 'last_Name' in request.form:
            if session:
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
                url = request.form['file']
                # upload_image(url)
                about = request.form['about_me']
                facebook = request.form['facebook']
                instagram = request.form['instagram']
                if first_time == 'on':
                    first_time_res = True
                else:
                    first_time_res = False
                user = User(email, None, None, None, first_name,
                            last_name, Age, first_time_res, destination,
                            start_date, end_date, language, budget, hobbies, vibe, url, about, facebook, instagram)
                user.update_user()
                print(email)
                print(url)
                return redirect('/MyProfile')
            else:
                return render_template('createProfile.html', message='User must login/signin first')
    return render_template('createProfile.html')


# class Upload(dbManager.Model):
#     id = dbManager.Column(dbManager.Intger, primary_key=True)
#     filename = dbManager.Column(dbManager.String(50))
#     data = dbManager.Column(dbManager.LargeBinary)



# def upload_image(file):
#     filename = secure_filename(file.filename)
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
