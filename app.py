import flask_login
from flask import Flask, render_template, session, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user

from User import User
from db import DB

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = DB()
login_manager = LoginManager()
login_manager.init_app(app)


# TODO
# Setup DB connections
# Setup HTML forms
# CSS?
# Handle POST requests
# Create views for all interactions
# ...

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route('/', methods=["GET"])
def index():
    if 'username' not in session:
        print("IMPLEMENT USERS")
    return render_template('index.html')


@app.route('/reception', methods=["GET"])
@login_required
def receptionist_portal():
    return render_template('reception.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        remember = request.form.get("remember")

        try:
            actual_pass = db.query("SELECT password FROM \"User\" WHERE username LIKE '" + username + "';").pop()[0]
            if password == actual_pass:
                login_user(load_user(username))
                print(flask_login.current_user.id)  # Print Current User's username

            return redirect("/reception")
        except IndexError as e:
            print(e)

    return render_template('login.html')


if __name__ == '__main__':
    app.run()
