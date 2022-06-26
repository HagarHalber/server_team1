from datetime import timedelta

from flask import Flask, jsonify, session, redirect

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)


@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))

###### Pages
## createProfile
from pages.CreateProfile.CreateProfile import createProfile

app.register_blueprint(createProfile)

from pages.UpdateProfile.UpdateProfile import updateProfile

app.register_blueprint(updateProfile)

from pages.HomePage.HomePage import Home

app.register_blueprint(Home)

from pages.AboutUs.AboutUs import About

app.register_blueprint(About)

from pages.ContectUs.ContectUs import ContectUs

app.register_blueprint(ContectUs)

from pages.ContectUs_signin.ContectUs_signin import ContectUsSignin

app.register_blueprint(ContectUsSignin)

from pages.MyMatches.MyMatches import MyMatches

app.register_blueprint(MyMatches)

from pages.MyProfile.MyProfile import MyProfile

app.register_blueprint(MyProfile)

from pages.SignUp.SingUp import SignUp

app.register_blueprint(SignUp)

@app.route('/log_out')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect('/Home')


if __name__ == '__main__':
    app.run(debug=True)
